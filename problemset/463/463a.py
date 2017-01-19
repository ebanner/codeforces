if __name__ == '__main__':
    n, s = [int(num) for num in raw_input().split()]
    P = [[int(num) for num in raw_input().split()] for _ in range(n)]

    max_sweet = -1
    for x, y in P:
        if x > s:
            continue
        elif y == 0:
            max_sweet = max(max_sweet, 0)
            continue

        max_sweet = max(100-y, max_sweet)

    print max_sweet
