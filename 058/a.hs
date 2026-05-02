getMessage = getLine


main = do
  message <- getMessage

  let
    message' = message ++ "."
    result = foldr go (const False) message' 0
    go c cont j
      | j == length "hello" = True
      | c == "hello" !! j = cont (j+1)
      | otherwise = cont j

  putStrLn $
    if result then "YES" else "NO"
