getMessage = getLine


main = do
  message <- getMessage

  let
    n = length message
    result = foldr go (const False) [0..n] 0

    go i cont 5 = True
    go i cont j
      | i == n = False
      | message !! i == "hello" !! j = cont (j+1)
      | otherwise = cont j

  in
    putStrLn $
      if result then "YES" else "NO"
