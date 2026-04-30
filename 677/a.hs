getH :: IO Int
getH = do
  line <- getLine
  let [_, h] = map read $ words line
  return h


getHeights :: IO [Int]
getHeights = do
  line <- getLine
  let heights = map read $ words line
  return heights


getWidth :: Int -> (Int -> Int)
getWidth h = (+1) . fromEnum . (>h)


main = do
  h <- getH
  heights <- getHeights

  let
    widths = map (getWidth h) heights

  print $ sum widths
