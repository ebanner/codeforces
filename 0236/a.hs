getUsername :: IO String
getUsername = do
  getLine


main = do
  username <- getUsername

  print $ 
    if length username `mod` 2 == 0
       then "CHAT WITH HER!"
       else "IGNORE HIM!"
