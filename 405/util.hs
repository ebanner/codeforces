type Grid = Map (Int, Int) Int


getRow :: Grid -> Int -> [Int]
getRow grid i =
  let
    ((_,m'), _) = Map.findMax grid
  in
    [grid Map.! (i,j) | j <- [0..m']]


showGrid :: Grid -> String
showGrid grid =
  let
    ((n',_), _) = Map.findMax grid
  in
    intercalate "\n" $
      map show [getRow grid i | i <- [0..n']]


getData :: Grid -> Array (Int, Int) Int
getData grid =
  let
    ((n',m'), _) = Map.findMax grid
  in
    listArray
      ((0,0), (n',m'))
      [grid Map.! (i,j) | i <- [0..n'], j <- [0..m']]


-- let
--   grid' = getData $ shake grid
-- in
--   forM_ [0..2] $ \i ->
--     print [grid' ! (i,j) | j <- [0..3]]

