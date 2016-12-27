if __name__ == '__main__':
    raw_input() # discard n

    R, G, B = range(3)
    state = -1

    color_str = raw_input()
    color = color_str[0]
    if color == 'R':
        state = R
    elif color == 'G':
        state = G
    else:
        assert color == 'B'
        state = B

    num_dups = 0
    for color in color_str[1:]:
        if color == 'R':
            if state == R:
                num_dups += 1
            state = R
        elif color == 'G':
            if state == G:
                num_dups += 1
            state = G
        else:
            assert color == 'B'
            if state == B:
                num_dups += 1
            state = B

    print num_dups
