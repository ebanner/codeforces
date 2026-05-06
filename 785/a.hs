import qualified Data.Map as Map


getPolyhedras :: IO [String]
getPolyhedras = do
  n <- read <$> getLine
  polyhedras <- sequence (replicate n getLine)
  return polyhedras


main = do
  polyhedras <- getPolyhedras

  let
    shapes = Map.fromList [
      ("Tetrahedron", 4),
      ("Cube", 6),
      ("Octahedron", 8),
      ("Dodecahedron", 12),
      ("Icosahedron", 20)]

    sides = map (shapes Map.!) polyhedras

  print $ sum sides
