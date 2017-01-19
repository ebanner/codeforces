from collections import defaultdict

if __name__ == '__main__':
    n = int(raw_input())
    R = [raw_input().split() for _ in range(n)]

    S = defaultdict(int)
    for name, points in R:
        points = int(points)
        S[name] += points

        if points >= 0: # check to see if this person is new leader
            if S[name] < max(p for n, p in S.items() if not n == name):
                leader = name
        elif points < 0:
