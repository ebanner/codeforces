if __name__ == '__main__':
    n, k = [int(num) for num in raw_input().split()]

    num_odd = n/2 if n % 2 == 0 else n/2 + 1

    if k <= num_odd:
        print 2*k - 1
    else:
        k -= num_odd
        print 2*k
