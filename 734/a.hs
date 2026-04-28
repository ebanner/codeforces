getWinners :: IO String
getWinners = do
  line <- getLine
  getLine


count :: [Bool] -> Int
count bools = sum $ map fromEnum $ bools


main = do
  winners <- getWinners

  let
    antonWins = count $ map ('A'==) winners
    n = length winners
    mid = fromIntegral n / 2
    result
      | fromIntegral antonWins < mid = "Danik"
      | fromIntegral antonWins == mid = "Friendship"
      | fromIntegral antonWins > mid = "Anton"

  putStrLn result

