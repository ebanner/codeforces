getN :: IO Int
getN = readLn


main = do
  n <- getN

  let
    f 0 = 0
    f n = (-1)^n * n + f (n-1)

  print $ f n

