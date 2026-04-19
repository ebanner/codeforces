import Data.List (sort, intercalate)
import Data.List.Split (splitOn)


getExpression :: IO String
getExpression = getLine


main = do
  expression <- getExpression

  print $ intercalate "+" $ sort $ splitOn "+" expression
