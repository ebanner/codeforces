if __name__ == '__main__':
    n = int(raw_input())

    table = [[0]*100 for _ in range(100)]
    for _ in range(n):
        x1, y1, x2, y2 = [int(num)-1 for num in raw_input().split()] # zero-index

        for i in range(y1, y2+1):
            for j in range(x1, x2+1):
                table[i][j] += 1

    print sum(elem for row in table for elem in row)
