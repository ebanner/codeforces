getBerlandishWord = getLine
getBirlandishWord = getLine


main = do
  berlandishWord <- getBerlandishWord
  birlandishWord <- getBirlandishWord

  putStrLn $
    if reverse berlandishWord == birlandishWord
      then "YES"
      else "NO"
