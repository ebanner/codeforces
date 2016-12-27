from collections import defaultdict

if __name__ == '__main__':
    n = int(raw_input())
    S = raw_input()

    D = defaultdict(int)
    for s in S:
        D[s] += 1

    nb_change = 0
    for letter, count in D.iteritems():
        nb_change += max(count-1, 0)

    print nb_change
