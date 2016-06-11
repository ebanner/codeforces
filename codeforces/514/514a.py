if __name__ == '__main__':
    x = [int(num) for num in list(raw_input())]

    inverted = [min(d, 9-d) for d in x]

    i = 0
    while inverted[i] == 0:
        inverted[i] = 9 # undo leading zeros

    print ''.join(str(d) for d in inverted)
