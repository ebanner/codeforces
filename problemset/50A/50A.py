if __name__ == '__main__':
    M, N = raw_input().split()
    M, N = [int(num) for num in (M, N)]

    if M == N == 1:
        num_dominos = 0
    elif M == 1:
        num_dominos = N / 2
    else:
        num_dominos = N
        num_dominos *= (M/2)

        if M % 2 == 1:
            num_dominos += (N/2)

    print num_dominos
