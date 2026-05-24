import Data.Bool (bool)


parse :: String -> (Int, Int, Int)
parse line = (a, b, c)
  where
    [a, b, c] = map read $ words line
    

getTestCases :: IO [(Int, Int, Int)]
getTestCases = do
  t <- readLn
  lines <- sequence (replicate t getLine)
  return $ map parse lines


isSum :: (Int, Int, Int) -> Bool
isSum (a, b, c)
  | a+b == c = True
  | a+c == b = True
  | b+c == a = True
  | otherwise = False


main = do
  testCases <- getTestCases

  let
    n = length testCases
    serialize = bool "NO" "YES"
    results = map (serialize . isSum) testCases

  mapM_ putStrLn results
