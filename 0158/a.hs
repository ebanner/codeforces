import Data.Function ((&))


getScores :: IO (Int, [Int])
getScores = do
  [n, k] <- (map read . words) <$> getLine
  scores <- (map read . words) <$> getLine
  return (k, scores)


main = do
  (k, scores) <- getScores

  let threshold = scores !! (k-1)

  [() | score <- scores,
        score > 0,
        score >= threshold] & length & print
