import sys

if __name__ == '__main__':
    n = int(raw_input())

    times = sorted(tuple(int(num) for num in raw_input().split()) for _ in range(n))

    l, s = zip(*times)
    for s1, s2 in zip(s, s[1:]):
        if s1 > s2:
            break
    else:
        # non-decreasing sequence
        print max(s)
        sys.exit()

    print max(l)
