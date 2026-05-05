import Control.Monad (forM_)
import Data.Array
import Data.List (intercalate)
import Data.Map.Strict (Map)
import qualified Data.Map.Strict as Map
import Data.Maybe (listToMaybe)


fixedPoint :: Eq a => (a -> a) -> a -> a
fixedPoint f =
  let 
    fixed x = f x == x
  in
    until fixed f


getColumns :: IO [Int]
getColumns = do
  getLine
  line <- getLine
  let columns = map read $ words line
  return columns


type Grid = Map (Int, Int) Int


ref :: Grid -> (Int, Int) -> Int
ref grid (i,j) =
  grid Map.! (i,j)


getGrid :: [Int] -> Grid
getGrid columns =
  let
    n = maximum columns
    m = length columns
  in
    Map.fromList [
      ((i,j), if y <= c then 1 else 0)
        | i <- [0..n-1],
          j <- [0..m-1],
          let c = columns !! j,
          let y = n-i]


isLoose :: Grid -> (Int, Int) -> Bool
isLoose grid (i,j) =
  let
    ((_,m'), _) = Map.findMax grid
  in
    if j == m'
       then False
       else grid `ref` (i,j) == 1 &&
            grid `ref` (i,j+1) == 0


findLoose :: Grid -> Maybe (Int, Int)
findLoose grid =
  let
    ((n',m'), _) = Map.findMax grid
  in
    listToMaybe $
      [(i,j) | i <- [0..n'],
               j <- [0..m'],
               isLoose grid (i,j)]


nudge :: Grid -> (Int, Int) -> Grid
nudge grid (i,j) = do
  Map.insert (i,j) 0 $ Map.insert (i,j+1) 1 grid


shake :: Grid -> Grid
shake grid =
  case findLoose grid of
    Nothing -> grid
    Just (i,j) -> nudge grid (i,j)


toColumns :: Grid -> [Int]
toColumns grid =
  let
    ((n',m'), _) = Map.findMax grid
    init = Map.fromList [(j,0) | j <- [0..m']]
    columns = foldl go init [(i,j) | i <- [0..n'], j <- [0..m']]
    go columns (i,j)
      | grid Map.! (i,j) == 1 = Map.adjust (+1) j columns
      | otherwise = columns
  in
    [columns Map.! j | j <- [0..m']]


main = do
  columns <- getColumns

  let
    grid = getGrid columns
    grid' = fixedPoint shake grid

  putStrLn $ unwords $ map show $ toColumns grid'
