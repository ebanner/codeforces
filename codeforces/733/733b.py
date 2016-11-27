from itertools import count

if __name__ == '__main__':
    n = int(raw_input())
    L, R = zip(*([int(num) for num in raw_input().split()] for _ in range(n)))

    nb_left, nb_right = sum(L), sum(R)
    max_beauty, max_j = abs(nb_left - nb_right), 0
    for i, l, r in zip(count(start=1), L, R):
        new_beauty = abs((nb_left-l+r)-(nb_right-r+l))
        if new_beauty > max_beauty:
            max_j = i

    print max_j
