getStones :: IO String
getStones = do
  getLine
  getLine


del :: Int -> String -> String
del idx stones =
  [stone | (i, stone) <- zip [0..] stones, i /= idx]


findDuplicate :: String -> Int
findDuplicate stones =
  let
    idx = foldr __ (-1) (zip [0..] $ zip stones $ tail stones)
    __                  (idx, (s1, s2)) rest

      | s1 == s2 = idx
      | otherwise = rest
  in
    idx


delete :: String -> String
delete stones =
  del (findDuplicate stones) stones


hasNoDuplicates :: String -> Bool
hasNoDuplicates stones =
  and [s1 /= s2 | (s1, s2) <- zip stones $ tail stones]


main = do
  stones <- getStones

  let
    result = go stones 0
    go          stones numStones

      | hasNoDuplicates stones = numStones
      | otherwise = go (delete stones) (numStones+1)

  print result
