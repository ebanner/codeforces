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


getWidths :: [Bool] -> [Int]
getWidths heights =
  map ((+1) . fromEnum) heights


main = do
  h <- getH
  heights <- getHeights

  let
    widths = getWidths $ map (>h) heights

  print $ sum widths

