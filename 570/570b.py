if __name__ == '__main__':
    n, m = [int(num) for num in raw_input().split()]

    print 1 if n == m == 1 else m+1 if m-1 < n-m else m-1
