import Data.List.Split (splitOn)


getWeights :: IO (Int, Int)
getWeights = do
  weights <- splitOn " " <$> getLine
  let [l, b] = map read weights
  return (l, b)


main = do
  (l, b) <- getWeights

  let
    result = go (l, b) 0
    go          (l, b) numYears

      | l > b = numYears
      | otherwise = go (l*3, b*2) numYears+1

  putStrLn result
