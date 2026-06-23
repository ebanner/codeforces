n m ← 9 9

grid ← n m⍴ 0

grid[⍸ 2 | ⍳n;] ← 1

grid[(2,2+4×⍳n)[⍸ (2,2+4×⍳n) ≤ n];m] ← 1

grid[(4×⍳n)[⍸ (4×⍳n) ≤ n];1] ← 1

⎕ ← '.#'[1 + grid]
