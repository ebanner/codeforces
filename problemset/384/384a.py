if __name__ == '__main__':
    n = int(raw_input())

    board = [['.']*n for _ in range(n)]

    for i, row in enumerate(board):
        size = len(row[i%2::2])
        board[i][i%2::2] = ['C']*size

    for row in board:
        print ''.join(row)
