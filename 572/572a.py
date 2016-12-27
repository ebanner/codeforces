if __name__ == '__main__':
    n_a, n_b = [int(num) for num in raw_input().split()]
    k, m = [int(num) for num in raw_input().split()]
    A = [int(num) for num in raw_input().split()]
    B = [int(num) for num in raw_input().split()]

    print 'YES' if A[k-1] < B[-m] else 'NO'
