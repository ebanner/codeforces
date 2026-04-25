main = do
  location <- getLocation

  print $ location `div` 5 + if location `mod` 5 > 0
                                then 1
                                else 0
