if __name__ == '__main__':
    n, m = [int(num) for num in raw_input().split()]

    i = 0
    while True:
        nb_chip = i+1
        if m < nb_chip:
            break

        m -= nb_chip # give chip to walrus
        i = (i+1) % n

    print m
