getDimensions :: IO (Int, Int, Int)
getDimensions = do
  line <- getLine
  let [n, m, a] = map read (words line)
  return (n, m, a)


main = do
  (n, m, a) <- getDimensions

  print $ ceiling (fromIntegral n / fromIntegral a) *
          ceiling (fromIntegral m / fromIntegral a)
