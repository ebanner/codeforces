if __name__ == '__main__':
    n, x = [int(num) for num in raw_input().split()]
    C = [int(num) for num in raw_input().split()]

    C = sorted(C)
    nb_hour = 0
    for c in C:
        nb_hour += c*x
        x = max(x-1, 1)

    print nb_hour
