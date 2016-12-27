if __name__ == '__main__':
    n = int(raw_input())

    table = [[0]*n for _ in range(n)]

    for i in range(n):
        table[i][0] = table[0][i] = 1

    for i in range(1, n):
        for j in range(1, n):
            table[i][j] = table[i][j-1] + table[i-1][j]

    print table[n-1][n-1]
