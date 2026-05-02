getMessage = getLine


main = do
  message <- getMessage

  let
    n = length message
    m = length "hello"

    result = foldr go id [0..n-1] 0

    go i cont j
      | j == m = m
      | (message !! i) == ("hello" !! j) = cont (j+1)
      | otherwise = cont j

  putStrLn $
    if result == m then "YES" else "NO"
