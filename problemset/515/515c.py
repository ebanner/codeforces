map = {
        2: [2],
        3: [3],
        4: [2, 2, 3],
        5: [5],
        6: [3, 5],
        7: [7],
        8: [2, 2, 2, 7],
        9: [3, 3, 2, 7]
}

def __a__(a):
    for digit in a:
        if digit == 0 or digit == 1:
            continue

        for d in map[digit]:
            yield str(d)

if __name__ == '__main__':
    n = int(raw_input())
    a = [int(c) for c in raw_input()]

    print ''.join(sorted(__a__(a), reverse=True))
