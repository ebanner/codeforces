import Data.Char (toUpper)


getWord :: IO String
getWord = getLine


capitalize :: String -> String
capitalize word = 
  toUpper (head word) : tail word


main = do
  word <- getWord

  putStrLn $ capitalize word

