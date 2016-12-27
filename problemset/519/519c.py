if __name__ == '__main__':
    n, m = [int(num) for num in raw_input().split()]

    nb_team = 0
    while True:
        if m < 0 or n < 0:
            break

        if n > m:
            n -= 2
            m -=1
        else:
            m -= 2
            n -= 1

        nb_team += 1

    print nb_team - 1
