import sys
from collections import defaultdict

if __name__ == '__main__':
    n, x0, y0 = [int(num) for num in raw_input().split()]
    S = [[int(num) for num in raw_input().split()] for _ in range(n)]

    if all((x1, y1) == (x0, y0) for x1, y1 in S):
        print 1
        sys.exit()

    # Create lines
    L = set()
    for x1, y1 in S:
        if x1 == x0 and not y1 == y0:
            L.add('v') # add special
            continue

        m = (y1 - y0) / float(x1 - x0)
        b = y0 - m*x0
        L.add((m, b))

    print len(L)
