parse :: String -> (Int, Int)
parse line =
  let
    [p, q] = map read $ words line
  in
    (p, q)


getCapacities :: IO [(Int, Int)]
getCapacities = do
  n <- read <$> getLine
  lines <- sequence (replicate n getLine)
  return $ map parse lines


count :: [Bool] -> Int
count = sum . map fromEnum


main = do
  capacities <- getCapacities

  print $
    count $
      map ((>=2) . abs . uncurry (-)) capacities
