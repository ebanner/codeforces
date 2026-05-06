getCounts :: IO (Int, Int, Int, Int, Int)
getCounts = do
  lines <- sequence (replicate 5 getLine)
  let [k, l, m, n, d] = map read lines
  return (k, l, m, n, d)


main = do
  (k, l, m, n, d) <- getCounts

  let 
    result = foldl go 0 [1..d]
    go numDragonsHarmed i
      | i `rem` k == 0 ||
        i `rem` l == 0 ||
        i `rem` m == 0 ||
        i `rem` n == 0 = numDragonsHarmed + 1
      | otherwise = numDragonsHarmed

  print result
