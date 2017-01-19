from collections import defaultdict

if __name__ == '__main__':
    n = int(raw_input())
    S = raw_input()

    D = defaultdict(int)
    for s in S:
        D[s] += 1

    print 'Anton' if D['A'] > D['D'] else 'Danik' if D['D'] > D['A'] else 'Friendship'
