parse :: String -> (Int, Int, Int)
parse vectorLine =
  let
    [x, y, z] = map read $ words vectorLine
  in
    (x, y, z)


getVectors :: IO [(Int, Int, Int)]
getVectors = do

  n <- read <$> getLine

  vectorLines <- sequence (replicate n getLine)

  let vectors = map parse vectorLines

  return vectors


main = do
  vectors <- getVectors

  let
    result = foldl __ (head vectors) (tail vectors)
    __                (x, y, z) (tx, ty, tz) =

      (x+tx, y+ty, z+tz)

  putStrLn $
    if result == (0, 0, 0)
      then "YES"
      else "NO"
