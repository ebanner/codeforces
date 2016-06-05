weights = {
    'q': 9,
    'r': 5,
    'b': 3,
    'n': 3,
    'p': 1,
}


if __name__ == '__main__':
    board = [list(raw_input()) for _ in range(8)]

    white = black = 0
    for row in board:
        for piece in row:
            if piece.lower() in '.k':
                continue

            if piece.isupper():
                white += weights[piece.lower()]
            else:
                black += weights[piece.lower()]

    print 'White' if white > black else 'Black' if black > white else 'Draw'
