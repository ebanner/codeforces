getPositions :: IO String
getPositions = getLine


getWindow :: String -> Int -> String
getWindow positions i =
  take 7 $ drop i positions


same :: String -> Bool
same (x:xs) =
  and $ map (==x) xs


main = do
  positions <- getPositions

  let
    n = length positions
    dangerous = foldr __ False [0..n-7]
    __ i rest =
      let 
        window = getWindow positions i
      in
        if same window
           then True
           else rest

  putStrLn $
    if dangerous then "YES" else "NO"

