if __name__ == '__main__':
    n, m = [int(num) for num in raw_input().split()]

    nb_on = 0
    for _ in range(n):
        floor = [int(num) for num in raw_input().split()]

        for w1, w2 in zip(floor[::2], floor[1::2]):
            nb_on += w1 | w2

    print nb_on
