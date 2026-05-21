getOpinions :: IO [Int]
getOpinions = do
  getLine
  line <- getLine
  let opinions = map read $ words line
  return opinions


main = do
  opinions <- getOpinions

  putStrLn $
    if any (==1) opinions
      then "HARD"
      else "EASY"
