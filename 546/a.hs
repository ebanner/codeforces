getInput :: IO (Int, Int, Int)
getInput = do
  [k, n, w] <- map read . words <$> getLine
  return (k, n, w)


main = do
  (k, n, w) <- getInput

  let cost = sum $ map (*k) [1..w]

  print $ max (cost-n) 0

