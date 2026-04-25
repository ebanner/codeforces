import Data.Char (toLower, toUpper, isLower, isUpper)


getWord :: IO String
getWord = getLine


count :: [Bool] -> Int
count lst =
  sum . map fromEnum $ lst


numLower :: String -> Int
numLower s =
  count $ map isLower s


numUpper :: String -> Int
numUpper s =
  count $ map isUpper s


main = do
  s <- getWord

  putStrLn $
    if numLower s >= numUpper s
             then map toLower s
             else map toUpper s

