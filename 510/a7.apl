n m ← 9 9

grid ← n m⍴ 0

l r←(4×⍳n) (2,2+4×⍳n)

(grid[⍸2|⍳n;]) (grid[r[⍸r≤n];m]) (grid[l[⍸l≤n];1]) ← 1

⎕ ← '.#'[1 + grid]
