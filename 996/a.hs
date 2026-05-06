getDollars :: IO Int
getDollars =
  read <$> getLine


main = do
  n <- getDollars

  let
    denominations = [100, 20, 10, 5, 1]

    result = go n 0

    go 0 _ = 0
    go n 4 = (1+) $ go (n-1) 4
    go n j
      | n < denominations !! j = go n (j+1)
      | otherwise = (1+) $ go (n-denominations!!j) j

  print result
