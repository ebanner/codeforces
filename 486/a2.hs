getN :: IO Int
getN = readLn


main = do
  n <- getN

  let
    f = zipWith (*) (cycle [-1,1]) [1..]

  print $
    sum $
      take n $
        f
