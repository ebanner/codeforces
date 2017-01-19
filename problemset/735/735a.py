import sys
import operator

if __name__ == '__main__':
    n, k = [int(num) for num in raw_input().split()]
    C = raw_input()

    g = [i for i, c in enumerate(C) if c == 'G'][0]
    t = [i for i, c in enumerate(C) if c == 'T'][0]

    op = operator.add if g < t else operator.sub
    while True:
        g = op(g, k)

        if g < 0 or g >= n:
            break

        if C[g] == 'T':
            print 'YES'
            sys.exit()

        if C[g] == '#':
            break

    print 'NO'
