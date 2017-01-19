if __name__ == '__main__':
    Y, W = [int(num) for num in raw_input().split()]

    n = max(Y, W)

    P = {1: [],
         2: [2],
         3: [3],
         4: [2, 2],
         5: [5],
         6: [2, 3]}

    numer = P[6-n+1][:]
    denom = P[6][:]

    new_numer = []
    for n in numer:
        if n in denom:
            denom.remove(n)
        else:
            new_numer.append(n)

    numer_prod = 1
    for n in new_numer:
        numer_prod *= n

    denom_prod = 1
    for d in denom:
        denom_prod *= d

    print '{}/{}'.format(numer_prod, denom_prod)
