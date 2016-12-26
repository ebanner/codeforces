import sys
from collections import defaultdict

if __name__ == '__main__':
    k = int(raw_input())
    s = raw_input()

    if not len(s) % k == 0:
        print -1
        sys.exit()

    D = defaultdict(int)
    for letter in s:
        D[letter] += 1

    for letter, count in D.items():
        if not count % k == 0:
            print -1
            sys.exit()

    print ''.join(letter*(count/k) for letter, count in D.items()) * k
