parse :: String -> (Int, Int)
parse line =
  let
    [a, b] = map read $ words line
  in
    (a, b)


getStops :: IO [(Int, Int)]
getStops = do
  n <- read <$> getLine
  lines <- sequence (replicate n getLine)
  let stops = map parse lines
  return stops


main = do
  stops <- getStops

  let
    (_, minCapacity) = foldl go (0, 0) stops
    go (numPeople, maxPeople) (a, b) =
      let
        numPeople' = (numPeople-a) + b
      in
        (numPeople', max numPeople' maxPeople)

  print minCapacity
