import Data.Array (Array, listArray)
import Data.List (intercalate)
import Data.Map.Strict (Map)
import qualified Data.Map.Strict as Map


getDimensions :: IO (Int, Int)
getDimensions = do
  line <- getLine
  let [n, m] = map read $ words line
  return (n, m)


type Grid a = Map (Int, Int) a

getHeight :: Grid Char -> Int
getHeight grid =
    fromEnum $ grid Map.! (-1,0)


getWidth :: Grid Char -> Int
getWidth grid =
    fromEnum $ grid Map.! (-1,1)


getRow :: Grid Char -> Int -> [Char]
getRow grid i =
  let
    m = getWidth grid
  in
    [grid Map.! (i,j) | j <- [0..m-1]]


showGrid :: Grid Char -> String
showGrid grid =
  let
    n = getHeight grid
  in
    intercalate "\n" $
      map show [getRow grid i | i <- [0..n-1]]


getGrid :: (Int, Int) -> Grid Char
getGrid (n, m) = Map.fromList $
  [((-1,0), toEnum n), ((-1,1), toEnum m)] ++
    [((i,j), '.') | i <- [0..n-1], j <- [0..m-1]]


data Direction = North | East | South | West deriving (Eq)

type Index = (Int, Int)

draw :: Grid Char -> Index -> Direction -> Int -> Grid Char
draw grid (i,j) direction ticks
  | direction == South && i == n-1 = grid

  | direction == South && j == m-1 && ticks == 0 =
      draw
        (Map.insert (i,j) '#' grid)
        (i,j)
        West
        -1

  | direction == South && j == 0 && ticks == 0 =
      draw
        (Map.insert (i,j) '#' grid)
        (i,j)
        East
        -1

  | direction == East && j == m-1 =
      draw
        (Map.insert (i,j) '#' grid)
        (i,j)
        South
        3

  | direction == South && i == n-1 =
      draw
        (Map.insert (i,j) '#' grid)
        (i,j)
        West
        -1

  | direction == West && i == 0 =
      draw
        (Map.insert (i,j) '#' grid)
        (i,j)
        South
        3

  | direction == East =
      draw
        (Map.insert (i,j+1) '#' grid)
        (i,j)
        direction
        -1

  | direction == West =
      draw
        (Map.insert (i,j-1) '#' grid)
        (i,j)
        direction
        -1

  | otherwise = error "Unreachable"

  where
    (n, m) = (getHeight grid, getWidth grid)


drawSnake :: Grid Char -> Grid Char
drawSnake grid = draw grid (0,0) East


main = do
  (n, m) <- getDimensions

  let emptyGrid = getGrid (n, m)

  drawSnake emptyGrid
