getNumber :: IO Int
getNumber = read <$> getLine


getDigits :: Int -> [Int]
getDigits n
  | n == 0 = []
  | otherwise = n `mod` 10 : getDigits (n `div` 10)


digits :: Int -> [Int]
digits n
  | n == 0 = [0]
  | otherwise = getDigits n


isLuckyDigit :: Int -> Bool
isLuckyDigit = (`elem` [4, 7])


count :: [Bool] -> Int
count lst = sum . map fromEnum $ lst


isLucky :: Int -> Bool
isLucky n =
  and $ map isLuckyDigit $ digits n


main = do
  n <- getNumber

  let numLucky = count $ map isLuckyDigit $ reverse $ digits n

  putStrLn $
    if isLucky numLucky
       then "YES"
       else "NO"
