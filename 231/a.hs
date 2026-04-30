import Data.Function ((&))

parse :: String -> (Int, Int, Int)
parse line = do
  let tokens = words line
  let [p, v, t] = map read tokens
  (p, v, t)


getProblemConfidencesList :: IO [(Int, Int, Int)]
getProblemConfidencesList = do
  n <- readLn
  lines <- sequence (replicate n getLine)
  return $ map parse lines


main = do
  problemConfidencesList <- getProblemConfidencesList

  [() | (p, v, t) <- problemConfidencesList,
        p+v+t >= 2

   ] & length & print
  
