from collections import defaultdict

if __name__ == '__main__':
    N = int(raw_input())
    lengths = [int(num) for num in raw_input().split()]

    d = defaultdict(int)
    for length in lengths:
        d[length] += 1

    print max(d.values()), len(set(lengths))
