import sys
from collections import deque

if __name__ == '__main__':
    D = raw_input()
    n = len(D)

    Q = deque()
    idx, prefix, mod = 0, '', 0
    Q.appendleft([idx, prefix, mod])

    while Q:
        idx, prefix, mod = Q.pop()
        if mod == 0 and prefix:
            print 'YES'
            print prefix
            sys.exit()

        if idx == n:
            continue # this thread has reached the end

        idx_, prefix_, mod_ = idx+1, prefix+D[idx], (((mod*2) % 8) + int(D[idx])) % 8
        for i, _, m in Q:
            if [idx_, mod_] == [i, m]:
                break # another thread already contains this information
        else:
            Q.appendleft([idx_, prefix_, mod_])

        idx_, prefix_, mod_ = idx+1, prefix, mod
        for i, _, m in Q:
            if [idx_, mod_] == [i, m]:
                break # another thread already contains this information
        else:
            Q.appendleft([idx_, prefix_, mod_])

    print 'NO'
