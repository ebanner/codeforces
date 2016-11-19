if __name__ == '__main__':
    n, k = [int(num) for num in raw_input().split()]
    A = [int(num) for num in raw_input().split()]

    B = [0]*(n-1)
    for i in range(n-1):
        B[i] = max(k - (A[i] + A[i+1]), 0)

    for i in range(n-1):
        A[i+1] += B[i]
        if i == n - 2:
            continue # don't adjust B's right neighbor if we're at the end of B

        B[i+1] = max(B[i+1]-B[i], 0)

    print sum(B)
    print ' '.join(str(a) for a in A)
