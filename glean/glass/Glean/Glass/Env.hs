{-
  Copyright (c) Meta Platforms, Inc. and affiliates.
  All rights reserved.

  This source code is licensed under the BSD-style license found in the
  LICENSE file in the root directory of this source tree.
-}

module Glean.Glass.Env
  (
    -- * Read-only configuration
    Config(..),

    -- * Session resources
    Env(..),
    IndexBackend(..),
  ) where

import Util.EventBase (EventBaseDataplane)
import Facebook.Fb303 (Fb303State)
import Logger.IO (Logger)
import Glean.Impl.ConfigProvider (ConfigAPI)

import Data.Text (Text)
import Control.Concurrent.STM ( TVar )

import qualified Glean
import qualified Glean.Repo as Glean
import qualified Glean.LocalOrRemote as Glean
import Glean.Backend.Remote (ThriftBackend)
import Glean.Util.Some ( Some )
import Glean.Util.Time ( DiffTimePoints )

-- | Init-time configuration
data Config = Config
  { listenPort :: Int
  , configKey :: Text
  , gleanService :: Glean.Service
  , serviceName :: Text
  , refreshFreq :: DiffTimePoints -- ^ refresh glean repos on this frequency
  , numWorkerThreads :: Maybe Int
  }

-- | Read-only, scoped, dynamic resources.
data Env = Env
  { evp :: EventBaseDataplane
  , cfgapi :: ConfigAPI
  , logger :: Logger
  , gleanBackend :: Some Glean.Backend
  , fb303 :: Fb303State
  , latestGleanRepos :: TVar Glean.LatestRepos
  , gleanIndexBackend :: IndexBackend
  }

-- | A backend to create incremental databases
newtype IndexBackend = IndexBackend (Maybe ThriftBackend)
