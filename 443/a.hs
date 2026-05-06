import qualified Data.Set as Set


getSetStr = getLine


main = do
  setStr <- getSetStr

  let
    letters = words $ filter (`notElem` ",{}") setStr
    result = foldl go Set.empty letters
    go letters c = Set.insert c letters

  print $ length result
