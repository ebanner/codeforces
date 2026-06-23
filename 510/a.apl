n m ← 9 9

grid ← n m⍴ 0

grid[⍸ 2 | ⍳n;] ← 1

indices ← 2 , 2 + 4 × ⍳n
indices ← indices[⍸ indices ≤ n]
grid[indices;m] ← 1

indices ← 4 × ⍳n
indices ← indices[⍸ indices ≤ n]
grid[indices;1] ← 1

⎕ ← '.#'[1 + grid]
