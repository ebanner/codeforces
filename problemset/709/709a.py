if __name__ == '__main__':
    n, b, d = [int(num) for num in raw_input().split()]
    A = [int(num) for num in raw_input().split()]

    nb_waste = nb_empty = 0
    for a in A:
        if a > b:
            continue # throw orange away

        nb_waste += a
        if nb_waste > d:
            nb_empty += 1
            nb_waste = 0

    print nb_empty
