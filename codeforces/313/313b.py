from itertools import izip
import time

import sys

times = []

if __name__ == '__main__':
    s = list(raw_input())
    m = int(raw_input())

    start = time.time()
    # precompute difference list
    A = [0] + [int(ss == sss) for ss, sss in zip(s, s[1:])]
    # A = [0]*len(s)
    # for i in range(len(s)-1):
    #     A[i+1] = s[i] == s[i+1]
    times.append(time.time() - start)

    start = time.time()
    SA, accum = [0]*len(A), 0
    for i, a in enumerate(A):
        accum += a
        SA[i] = accum
    times.append(time.time() - start)

    start = time.time()
    # ranges = [[int(num)-1 for num in raw_input().split()] for _ in range(m)]
    lines = sys.stdin.readlines()
    ranges = [[int(num)-1 for num in line.split()] for line in lines]
    times.append(time.time() - start)

    start = time.time()
    outputs = [str(SA[r]-SA[l]) for i, (l, r) in enumerate(ranges)]
    (time.time() - start)

    start = time.time()
    print '\n'.join(outputs)
    times.append(time.time() - start)

    # print times
