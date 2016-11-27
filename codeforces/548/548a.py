import sys

if __name__ == '__main__':
    S = raw_input()
    k = int(raw_input())

    s = len(S)
    n = s/k
    if not s / float(k) == int(n):
        print 'NO'
        sys.exit()

    for i in range(k):
        substr = S[i*n:(i+1)*n]
        if not list(substr) == list(reversed(substr)):
            print 'NO'
            break
    else:
        print 'YES'
