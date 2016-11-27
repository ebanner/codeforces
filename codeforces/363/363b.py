if __name__ == '__main__':
    n, k = [int(num) for num in raw_input().split()]
    H = [int(num) for num in raw_input().split()]

    min_h, j = k * 100, 0
    for i in range(n-k+1):
        window = H[i:i+k]
        if sum(window) < min_h:
            min_h, j = sum(window), i

    print j+1 # 1-based indexing
