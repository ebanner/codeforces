getMessage = getLine


main = do
  message <- getMessage

  let
    n = length message
    m = length "hello"

    result = foldr go id [0..n-1] m

    go _ _ 0 = 0
    go i cont j
      | (message !! i) == ("hello" !! (m-j)) = cont (j-1)
      | otherwise = cont j

  in
    putStrLn $
      if result == 0 then "YES" else "NO"
