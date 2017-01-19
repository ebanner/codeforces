from collections import defaultdict

if __name__ == '__main__':
    n = int(raw_input())
    S = raw_input()

    S = [s.lower() for s in S]
    K = defaultdict(int)
    nb_buy = 0
    for key, lock in zip(S[::2], S[1::2]):
        K[key] += 1
        if K[lock] <= 0:
            'no', lock
            nb_buy += 1
            K[lock] += 1

        K[lock] -= 1

    print nb_buy
