{-
  Copyright (c) Meta Platforms, Inc. and affiliates.
  All rights reserved.

  This source code is licensed under the BSD-style license found in the
  LICENSE file in the root directory of this source tree.
-}


module Glean.Handler
  ( Write(..)
  , State(..)
  , handler
  ) where

import Data.Maybe

import Facebook.Fb303

import Glean.GleanService.Service as Service
import Glean.Database.Types
import qualified Glean.Backend as Backend
import Glean.Backend (StackedDbOpts(..))
import Glean.Types as Thrift

data State = State
  { fb303State :: Fb303State
  , stEnv :: Env
  }

handler :: State -> GleanServiceCommand a -> IO a
handler State{..} req =
  let backend = Backend.LoggingBackend stEnv in -- log (most) requests
  case req of
    Service.GetSchemaInfo repo req ->
      Backend.getSchemaInfo backend repo req

    Service.ValidateSchema req -> Backend.validateSchema backend req

    Service.SendBatch cbatch -> Backend.enqueueBatch backend cbatch

    Service.FinishBatch handle -> Backend.pollBatch backend handle

    Service.SendJsonBatch repo batch ->
      Backend.enqueueJsonBatch backend repo batch

    Service.KickOff rq -> Backend.kickOffDatabase backend rq

    Service.Finalize repo -> Backend.finalizeDatabase backend repo

    Service.UpdateProperties repo set unset ->
      Backend.updateProperties backend repo set unset

    Service.GetWork rq -> Backend.getWork backend rq

    Service.WorkCancelled rq -> Backend.workCancelled backend rq

    Service.WorkHeartbeat rq -> Backend.workHeartbeat backend rq

    Service.WorkFinished rq -> Backend.workFinished backend rq

    Service.QueryFact repo id ->
      fromMaybe (Thrift.Fact 0 mempty mempty) <$>
        Backend.queryFact backend repo id

    Service.FirstFreeId repo -> Backend.firstFreeId backend repo

    Service.FactIdRange repo -> Backend.factIdRange backend repo

    Service.UserQueryFacts repo req ->
      Backend.userQueryFacts backend repo req

    Service.UserQuery repo query ->
      Backend.userQuery backend repo query

    Service.CompletePredicates repo ->
      Backend.completePredicates backend repo

    Service.DeriveStored repo pred ->
      Backend.deriveStored backend (const mempty) repo pred

    Service.PredicateStats repo Thrift.PredicateStatsOpts{..} ->
      Backend.predicateStats backend repo $
        if predicateStatsOpts_excludeBase then ExcludeBase else IncludeBase

    Service.ListDatabases l ->
      Backend.listDatabases backend l

    Service.GetDatabase repo -> Backend.getDatabase backend repo

    Service.DeleteDatabase repo -> Backend.deleteDatabase backend repo

    Service.Restore loc -> Backend.restoreDatabase backend loc

    SuperFacebookService c -> fb303Handler fb303State c
