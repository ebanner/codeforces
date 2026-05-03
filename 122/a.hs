getNumber :: IO Int
getNumber = read <$> getLine


main = do
  n <- getNumber

  let
    luckyDivisorCandidates = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 777]
    result = foldr go False luckyDivisorCandidates
    go luckyDivisorCandidate rest

      | luckyDivisorCandidate > n = False
      | n `rem` luckyDivisorCandidate == 0 = True
      | otherwise = rest

  putStrLn $
    if result == True then "YES" else "NO"
