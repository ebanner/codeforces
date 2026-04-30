-- getWatermelonWeight = return 8

getWatermelonWeight :: IO Int
getWatermelonWeight = readLn -- return 8

canDivideEvenly :: Int -> Bool
canDivideEvenly w = w > 2 && even w 

main :: IO ()
main = do
  w <- getWatermelonWeight

  let result = if canDivideEvenly w
                 then "YES"
                 else "NO"

  putStrLn result
