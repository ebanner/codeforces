import Data.Char (toLower)


getStrings :: IO (String, String)
getStrings = do
  s <- getLine
  t <- getLine
  return (s, t)


main = do
  (s, t) <- getStrings

  let s' = map toLower s
  let t' = map toLower t

  let 
    result = foldr __ 0 (zip s' t')
    __ (a, b) rest

     | a < b = -1
     | a > b = 1
     | otherwise = rest

  print result
