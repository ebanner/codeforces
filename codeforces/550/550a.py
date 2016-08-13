import sys

if __name__ == '__main__':
    s = list(raw_input())
    n = len(s)

    ab, ba = [0]*n, [0]*n

    i, j = range(2)
    while j < n:
        if s[i] == 'A' and s[j] == 'B':
            ab[i] = ab[j] = 1
        elif s[i] == 'B' and s[j] == 'A':
            ba[i] = ba[j] = 1

        i, j = i+1, j+1

    nb_ab, nb_ba = sum(ab)/2, sum(ba)/2

    if nb_ab == 0 or nb_ba == 0:
        print 'NO'
    elif nb_ab == 1:
        i, j = range(2)
        while j < n:
            if not (s[i] == 'A' and s[j] == 'B'):
                i, j = i+1, j+1
                continue

            i_, j_ = max(i-1, 0), min(n-1, j+1)
            ba[i] = ba[j] = ba[i_] = ba[j_] = 0

            print 'NO' if sum(ba) == 0 else 'YES'
            break
    elif nb_ba == 1:
        i, j = range(2)
        while j < n:
            if not (s[i] == 'B' and s[j] == 'A'):
                i, j = i+1, j+1
                continue

            i_, j_ = max(i-1, 0), min(n-1, j+1)
            ab[i] = ab[j] = ab[i_] = ab[j_] = 0

            print 'NO' if sum(ab) == 0 else 'YES'
            break
    else:
        print 'YES'
