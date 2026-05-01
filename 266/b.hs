getT :: IO Int
getT = do
  line <- getLine
  let [_, t] = map read $ words line
  return t


shuffle :: String -> String
shuffle [] = []
shuffle [x] = [x]
shuffle (x:y:rest)
  | [x,y] == "BG" = "GB" ++ shuffle rest
  | otherwise = x : shuffle (y:rest)


main = do
  t <- getT
  line <- getLine

  let
    result = foldl go line [1..t]
    go line _ = shuffle line

  putStrLn result

