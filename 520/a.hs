import Data.Char (toLower)

import Data.Set (Set)
import qualified Data.Set as Set


getString :: IO String
getString = do
  getLine
  getLine


main = do
  string <- getString

  let
    letters = Set.fromList "abcdefghijklmnopqrstuvwxyz"

    result = foldr go id string letters

    go c rest letters
      | Set.null letters = letters
      | otherwise = rest $ Set.delete (toLower c) letters

  putStrLn $
    if Set.null result then "YES" else "NO"
