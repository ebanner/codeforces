getMessage = getLine


main = do
  message <- getMessage

  let
    result = foldr go id message "hello"

    go _ _ [] = []
    go c cont (d:ds)
      | c == d = cont ds
      | otherwise = cont (d:ds)

  putStrLn $
    if null result then "YES" else "NO"
