if __name__ == '__main__':
    P = list(raw_input())

    r, c = P
    r = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}[r]
    c = int(c)

    if 2 <= r <= 7 and 2 <= c <= 7:
        print 8
    elif abs(r-c) in [0, 7]:
        print 3
    else:
        print 5
