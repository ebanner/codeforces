import sys

def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a%b)

if __name__ == '__main__':
    l, r = [int(num) for num in raw_input().split()]

    for a in range(l, r-1):
        for b in range(a, r):
            if not gcd(b, a) == 1:
                continue

            for c in range(b, r+1):
                if not gcd(c, b) == 1:
                    continue

                if not gcd(c, a) == 1:
                    print a, b, c
                    sys.exit()

    print -1
