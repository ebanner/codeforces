import sys

if __name__ == '__main__':
    n = int(raw_input())

    if not n % 2 == 0:
        print -1
        sys.exit()

    evens = range(2, n+1, 2)
    odds  = range(1, n+1, 2)
    A = [0]*n
    A[::2], A[1::2] = evens, odds

    print ' '.join(str(a) for a in A)
