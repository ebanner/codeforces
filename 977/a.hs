getInput :: IO (Int, Int)
getInput = do
  line <- getLine
  let [n, k] = map read $ words line
  return (n, k)


main = do
  (n, k) <- getInput

  let
    result = foldl __ n [1..k]
    __                n _

      | n `mod` 10 == 0 = div n 10
      | otherwise = n-1

  print result
