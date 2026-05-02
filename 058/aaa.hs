getMessage = getLine


main = do
  message <- getMessage

  let
    message' = message ++ "."
    result = foldr go (const False) message' 0

    go c cont 5 = True
    go c cont j
      | c == "hello" !! j = cont (j+1)
      | otherwise = cont j

  in
    putStrLn $
      if result then "YES" else "NO"
