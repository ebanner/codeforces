if __name__ == '__main__':
    n, m = [int(num) for num in raw_input().split()]

    nb_sol = 0
    for i in range(n+1):
        for j in range(m+1):
            nb_sol += (i**2 + j == n) and (i + j**2 == m)

    print nb_sol
