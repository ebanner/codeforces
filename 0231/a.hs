import Data.Function ((&))

parse :: String -> [Int]
parse line = do
  let tokens = words line
  map read tokens


getProblemConfidencesList :: IO [[Int]]
getProblemConfidencesList = do
  n <- readLn
  lines <- sequence (replicate n getLine)
  return $ map parse lines


main = do
  problemConfidencesList <- getProblemConfidencesList

  [() | problemConfidences <- problemConfidencesList,
        sum problemConfidences >= 2

   ] & length & print
  
