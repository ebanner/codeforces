import sys
from itertools import izip, count

if __name__ == '__main__':
    S = [int(bit) for bit in raw_input()]
    T = [int(bit) for bit in raw_input()]

    edit_dist = sum(not s == t for s, t in izip(S, T))
    if not edit_dist % 2 == 0:
        print 'impossible'
        sys.exit()

    idx, bitstr = 0, [0]*len(S)
    for i, s, t in izip(count(), S, T):
        bitstr[i] = [s, t][idx]
        if not s == t:
            idx = (idx+1) % 2

    print ''.join(str(bit) for bit in bitstr)
