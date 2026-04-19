import Data.List (isPrefixOf, isSuffixOf)
import Data.Function ((&))


getStatements :: IO [String]
getStatements = do
  n <- readLn :: IO Int
  lines <- sequence (replicate n getLine)
  return lines


main = do
  statements <- getStatements

  let 
    step value statement
     | "++" `isPrefixOf` statement = value + 1
     | "++" `isSuffixOf` statement = value + 1
     | "--" `isPrefixOf` statement = value - 1
     | "--" `isSuffixOf` statement = value - 1
  in
    foldl step 0 statements & print
