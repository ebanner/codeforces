from collections import deque

if __name__ == '__main__':
    n, t, c = [int(num) for num in raw_input().split()]
    S = [int(num) for num in raw_input().split()]

    B = [s > t for s in S]
    Q = deque()
    nb_plus = 0
    for i in range(c):
        Q.appendleft((S[i], B[i]))
        nb_plus += B[i]

    nb_group = 1 if nb_plus == 0 else 0
    for i in range(c, n):
        _, larger = Q.pop()
        nb_plus -= larger
        Q.appendleft((S[i], B[i]))
        nb_plus += B[i]
        nb_group += 1 if nb_plus == 0 else 0

    print nb_group
