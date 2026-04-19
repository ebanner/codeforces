import Data.List (isPrefixOf, isSuffixOf)


getStatements :: IO [String]
getStatements = do
  n <- readLn :: IO Int
  lines <- sequence (replicate n getLine)
  return lines


main = do
  statements <- getStatements

  let 
    result = foldl step 0 statements
    step value statement
     | "++" `isPrefixOf` statement = value + 1
     | "++" `isSuffixOf` statement = value + 1
     | "--" `isPrefixOf` statement = value - 1
     | "--" `isSuffixOf` statement = value - 1
  in
    print result
