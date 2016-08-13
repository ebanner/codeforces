import sys

if __name__ == '__main__':
    n = int(raw_input())
    board = [list(raw_input()) for _ in range(n)]

    ds = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    for i in range(n):
        for j in range(n):
            nb_o = 0
            for dx, dy in ds:
                i_, j_ = i+dy, j+dx

                if not 0 <= i_ < n or not 0 <= j_ < n:
                    continue # off the board

                nb_o += board[i_][j_] == 'o'

            if nb_o % 2:
                print 'NO'
                sys.exit()

    print 'YES'
