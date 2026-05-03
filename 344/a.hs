getMagnets :: IO [String]
getMagnets = do
  n <- read <$> getLine
  magnets <- sequence (replicate n getLine)
  return magnets


doRepel :: (String, String) -> Bool
doRepel (m1, m2) =
  [m1, m2] == ["10", "01"] || [m1, m2] == ["01", "10"]


count :: [Bool] -> Int
count = sum . map fromEnum


main = do
  magnets <- getMagnets

  print $
    (1+) . count $
      map doRepel $ zip magnets $ tail magnets
