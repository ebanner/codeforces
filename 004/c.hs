import qualified Data.Map.Strict as Map
import qualified Data.Sequence as Seq


getRegistrationRequests :: IO [String]
getRegistrationRequests = do
  n <- read <$> getLine
  registrationRequests <- sequence (replicate n getLine)
  return registrationRequests


main = do
  registrationRequests <- getRegistrationRequests

  let
    (db, responses) = (Map.empty, Seq.empty)
    (_, responses') = foldl go (db, responses) registrationRequests

    go (db, responses) username =
      case Map.lookup username db of
        Just v  -> (Map.insert username (v+1) db, responses Seq.|> (username ++ show v))
        Nothing -> (Map.insert username 1 db, responses Seq.|> "OK")

    n = length responses'

  mapM_ putStrLn responses'

