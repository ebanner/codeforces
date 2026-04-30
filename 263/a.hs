import Data.Array
import Control.Monad


parse :: String -> [Int]
parse line = map read $ words line


getMatrix :: IO (Array (Int, Int) Int)
getMatrix = do
  lines <- sequence (replicate 5 getLine)
  let rows = map parse lines
  return $ listArray ((0,0), (5-1,5-1)) (concat rows)


main = do
  matrix <- getMatrix

  let (i, j) = head [(i, j) | i <- [0..4],
                              j <- [0..4],
                              matrix ! (i, j) == 1]

  print $ abs (2-i) + abs (2-j)

  -- forM_ [0..4] $ \i ->
  --   print [matrix ! (i, j) | j <- [0..4]]
