getMessage = getLine


main = do
  message <- getMessage

  let
    message' = message ++ "."
    result = foldr go (const False) message' "hello"

    go c cont [] = True
    go c cont (d:ds)
      | c == d = cont ds
      | otherwise = cont (d:ds)

  putStrLn $
    if result then "YES" else "NO"
