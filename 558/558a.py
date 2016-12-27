if __name__ == '__main__':
    n = int(raw_input())
    pairs = sorted(([int(num) for num in raw_input().split()] for _ in range(n)))

    X, A = zip(*pairs)
    L, R = [a for x, a in pairs if x < 0], [a for x, a in pairs if x > 0]

    nb_left, nb_right = len(L), len(R)
    if nb_left > nb_right:
        print sum(L[:nb_right+1]) + sum(R)
    elif nb_left < nb_right:
        print sum(L) + sum(R[:nb_left+1])
    else:
        print sum(L) + sum(R)
