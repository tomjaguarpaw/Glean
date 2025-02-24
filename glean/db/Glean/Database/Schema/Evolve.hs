{-
  Copyright (c) Meta Platforms, Inc. and affiliates.
  All rights reserved.

  This source code is licensed under the BSD-style license found in the
  LICENSE file in the root directory of this source tree.
-}

module Glean.Database.Schema.Evolve
  ( mkPredicateEvolution
  , evolvePat
  ) where

import Data.List (elemIndex)
import Data.Bifoldable
import qualified Data.Map.Strict as Map
import Data.Map.Strict (Map)
import Data.Maybe (fromMaybe, listToMaybe)
import Data.Text (Text)
import qualified Data.Set as Set
import Data.Word (Word64)

import Glean.Angle.Types (FieldDef_(..))
import qualified Glean.Angle.Types as Type
import Glean.Query.Codegen
import Glean.Database.Schema.Types
import qualified Glean.RTS as RTS
import Glean.RTS.Types
import Glean.RTS.Term (Value, Term(..))
import Glean.Schema.Util (lowerMaybe, lowerBool, lowerEnum)
import qualified Glean.Types as Thrift

mkPredicateEvolution
  :: (Pid -> PredicateDetails)
  -> Pid
  -> Pid
  -> Maybe PredicateEvolution
mkPredicateEvolution detailsFor oldPid newPid
  | oldPid == newPid = Nothing
  | otherwise = Just PredicateEvolution
    { evolutionOld = old
    , evolutionNew = new
    , evolutionEvolveKey = evolve
        (predicateKeyType old)
        (predicateKeyType new)
    , evolutionEvolveValue = evolve
        (predicateValueType old)
        (predicateValueType new)
    , evolutionDevolve = fromMaybe id $
        mkFactTransformation new old
    }
  where
      new = detailsFor newPid
      old = detailsFor oldPid
      evolve old new pat = evolvePat overUnit overVar old new pat
      overUnit _ _ () = ()
      overVar _ _ var = var

evolvePat :: (Show a, Show b)
  => (Type -> Type -> a -> c)
  -> (Type -> Type -> b -> d)
  -> Type
  -> Type
  -> Term (Match a b)
  -> Term (Match c d)
evolvePat innerL innerR old@(Type.NamedTy _) new pat =
  evolvePat innerL innerR (derefType old) new pat
evolvePat innerL innerR old new@(Type.NamedTy _) pat =
  evolvePat innerL innerR old (derefType new) pat
evolvePat innerL innerR old new pat = case pat of
  Byte x -> Byte x
  Nat x -> Nat x
  ByteArray x -> ByteArray x
  String x -> String x
  Ref match -> Ref $ case match of
    -- we can keep variable bindings as they are given any value of type T
    -- assigned to a variable will have been changed to type evolved(T).
    MatchBind var -> MatchBind $ innerR old new var
    MatchVar var -> MatchVar $ innerR old new var
    MatchWild _ -> MatchWild new
    MatchNever _ -> MatchNever new
    MatchFid fid -> MatchFid fid
    MatchAnd a b -> MatchAnd
      (evolve old new a)
      (evolve old new b)
    MatchPrefix prefix rest -> MatchPrefix prefix $ evolve old new rest
    MatchExt extra -> MatchExt $ innerL old new extra
  Alt oldIx term
    | Type.BooleanTy <- old
    , Type.BooleanTy <- new ->
        evolve lowerBool lowerBool pat
    | Type.Maybe oldTy <- old
    , Type.Maybe newTy <- new ->
        evolve (lowerMaybe oldTy) (lowerMaybe newTy) pat
    | Type.EnumeratedTy oldAlts <- old
    , Type.EnumeratedTy newAlts <- new ->
        evolve
          (lowerEnum oldAlts)
          (lowerEnum newAlts)
          pat
    | Type.Sum oldAlts <- old
    , Type.Sum newAlts <- new
    -- alternatives could change order
    , Just oldAlt <- oldAlts `maybeAt` fromIntegral oldIx
    , Just newIx <-
        elemIndex (fieldDefName oldAlt) (fieldDefName <$> newAlts)
    , Just newAlt <- newAlts `maybeAt` newIx ->
        Alt (fromIntegral newIx) $ evolve
          (fieldDefType oldAlt)
          (fieldDefType newAlt)
          term
  Array terms
    | Type.Array oldTy <- old
    , Type.Array newTy <- new ->
      Array $ evolve oldTy newTy <$> terms
  Tuple terms
    | Type.RecordTy oldFields <- old
    , Type.RecordTy newFields <- new
    ->  let termsMap = Map.fromList
              [ (name, (oldTy, term))
              | (FieldDef name oldTy, term) <- zip oldFields terms ]
            termForField  (FieldDef name newTy) =
              case Map.lookup name termsMap of
                Just (oldTy, term) -> evolve oldTy newTy term
                Nothing -> Ref (MatchWild newTy)
        in
        Tuple $ fmap termForField newFields
  _ -> error $ "unexpected pattern: " <> show (pat, old, new)
  where
    maybeAt list ix = listToMaybe (drop ix list)
    evolve = evolvePat innerL innerR

mkFactTransformation
  :: PredicateDetails
  -> PredicateDetails
  -> Maybe (Thrift.Fact -> Thrift.Fact)
mkFactTransformation from to
  | Nothing <- mTransformKey
  , Nothing <- mTransformValue = Nothing
  | otherwise = Just $ \(Thrift.Fact _ key value) ->
     Thrift.Fact
       (fromPid $ predicatePid to)
       (RTS.fromValue $ overKey $ RTS.toValue keyRep key)
       (RTS.fromValue $ overValue $ RTS.toValue valueRep value)
  where
    overKey = fromMaybe id mTransformKey
    overValue = fromMaybe id mTransformValue
    keyRep = repType $ predicateKeyType from
    valueRep = repType $ predicateValueType from
    mTransformKey = mkValueTransformation
      (predicateKeyType from)
      (predicateKeyType to)
    mTransformValue = mkValueTransformation
      (predicateValueType from)
      (predicateValueType to)

-- | Create a transformation from a term into another term of a compatible
-- type.  Returns Nothing if no change is needed.
mkValueTransformation :: Type -> Type -> Maybe (Value -> Value)
mkValueTransformation from to = go from to
  where
    names = map fieldDefName

    -- if an option's definition and index didn't change it
    -- will not have an entry in this map.
    transformationsFor
      :: [FieldDef]
      -> [FieldDef]
      -> Map Text (Word64, Value -> Value)
    transformationsFor from to = Map.fromList
      [ (name, (ixTo, f))
      | (FieldDef name defFrom, ixFrom) <- zip from [0..]
      , Just (ixTo, f) <- return $ do
          case Map.lookup name toFields of
            Nothing -> Just unknown
            Just (ixTo, defTo) ->
              case go defFrom defTo of
                Nothing | ixTo == ixFrom -> Nothing
                Nothing -> Just (ixTo, id)
                Just f -> Just (ixTo, f)
      ]
      where
        unknown = (fromIntegral (length to), const (Tuple []))

        toFields :: Map Text (Word64, Type)
        toFields = Map.fromList $ flip map (zip to [0..])
          $ \(FieldDef name def, ix) -> (name, (ix, def))

    go :: Type -> Type -> Maybe (Value -> Value)
    go from@(Type.NamedTy _) to = go (derefType from) to
    go from to@(Type.NamedTy _) = go from (derefType to)
    go Type.Byte Type.Byte = Nothing
    go Type.Nat Type.Nat = Nothing
    go Type.String Type.String = Nothing
    go Type.BooleanTy Type.BooleanTy = Nothing
    go (Type.Maybe from) (Type.Maybe to) = go (lowerMaybe from) (lowerMaybe to)
    go (Type.Predicate _) (Type.Predicate _) = Nothing
    go (Type.EnumeratedTy from) (Type.EnumeratedTy to) =
      go (lowerEnum from) (lowerEnum to)
    go (Type.Array from) (Type.Array to) = do
      f <- go from to
      return $ \term -> case term of
        Array vs -> Array (map f vs)
        _ -> error $ "expected Array, got " <> show term

    go (Type.RecordTy from) (Type.RecordTy to) =
      let transformationsMap = transformationsFor from to
          transformations =
            [ (field, transform)
            | field <- names to
            , transform <- [maybe id snd $ Map.lookup field transformationsMap]
            ]
          noChange = null transformationsMap
      in
      if noChange
      then Nothing
      else Just $ \term -> case term of
        Tuple contents -> Tuple
          [ transform content
          | (field, transform) <- transformations
          , Just content <- [lookup field withNames]
          ]
          where withNames = zip (names from) contents
        _ -> error $ "expected Tuple, got " <> show term

    go (Type.Sum from) (Type.Sum to) =
      let transformations = transformationsFor from to
          noChange = Map.null transformations
          altMap = Map.fromList
              [ (ixFrom, (ixTo, change))
              | (name, ixFrom) <- zip (names from) [0..]
              , Just (ixTo, change) <- [Map.lookup name transformations]
              ]
      in
      if noChange
        then Nothing
        else Just $ \term -> case term of
          Alt n content -> case Map.lookup n altMap of
            Nothing -> Alt n content
            Just (n', change) -> Alt n' (change content)
          _ -> error $ "expected Alt, got " <> show term
    go from to =
      error $ "invalid type conversion: "
        <> show from <> " to " <> show to
