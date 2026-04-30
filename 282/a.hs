import Data.List (isPrefixOf, isSuffixOf)


getStatements :: IO [String]
getStatements = do
  n <- readLn :: IO Int
  lines <- sequence (replicate n getLine)
  return lines


main = do
  statements <- getStatements

  let 
    x = foldl __ 0 statements
    __           x statement

     | "++" `isPrefixOf` statement = x+1
     | "++" `isSuffixOf` statement = x+1
     | "--" `isPrefixOf` statement = x-1
     | "--" `isSuffixOf` statement = x-1
  in
    print x
