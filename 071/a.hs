getWords :: IO [String]
getWords = do
  n <- readLn :: IO Int
  let lines = (replicate n getLine)
  sequence lines


abbreviate :: String -> String
abbreviate word = 
  [head word] ++ show (length word - 2) ++ [last word]


main = do
  words <- getWords

  let abbreviations =
       [ if length word > 10 then abbreviate word else word
         | word <- words
       ]

  mapM_ putStrLn abbreviations
