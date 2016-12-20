import random
from collections import deque

GOOD, BAD = '.', '-'
D = [(1, 0), (0, -1), (-1, 0), (0, 1)]
C = {'W': 'B', 'B': 'W'}


if __name__ == '__main__':
    n, m = [int(num) for num in raw_input().split()]
    B = [list(raw_input()) for _ in range(n)]

    G = set()
    for i in range(n):
        for j in range(m):
            if B[i][j] == GOOD:
                G.add((i, j))

    U = G # "goods" to "unexplored"
    while U:
        i, j = random.sample(U, k=1)[0]

        # exhaustive dfs
        s = deque()
        s.appendleft((i, j))
        while s:
            i, j = s.popleft()
            U.remove((i, j))

            # color cell based on neighbor colorings
            for di, dj in D:
                i_, j_ = min(max(i+di, 0), n-1), min(max(j+dj, 0), m-1)

                if i == i_ and j == j_:
                    continue # off the board

                if B[i_][j_] == BAD:
                    continue # bad cell has no impact on coloring

                if B[i_][j_] == '.':
                    continue # uncolored good cell has not impact on coloring
                
                color = B[i_][j_]
                B[i][j] = C[color]
                break

            else:
                B[i][j] = 'W' # arbitrarily color white because no colored neighbors

            # add cells to dfs stack
            for di, dj in D:
                i_, j_ = min(max(i+di, 0), n-1), min(max(j+dj, 0), m-1)

                if i == i_ and j == j_:
                    continue # off the board

                if B[i_][j_] == BAD:
                    continue # bad cell does not need to be explored

                if B[i_][j_] == 'W' or B[i_][j_] == 'B':
                    continue # colored cell already colored

                if (i_, j_) in s:
                    continue # already added to the frontier

                s.appendleft((i_, j_))

    for b in B:
        print ''.join(b)
