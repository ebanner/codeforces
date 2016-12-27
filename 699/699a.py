if __name__ == '__main__':
    n = int(raw_input())
    D = list(raw_input())
    X = [int(num) for num in raw_input().split()]

    min_dist = 1e9
    for i in range(n-1):
        if D[i] == 'R' and D[i+1] == 'L':
            min_dist = min(X[i+1] - X[i], min_dist)

    print min_dist / 2 if not min_dist == 1e9 else -1
