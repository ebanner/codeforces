if __name__ == '__main__':
    n = int(raw_input())

    nb_good, good_idxs = 0, []
    for i in range(1, n+1):
        row = [int(num) for num in raw_input().split()]
        nb_good += 1 if 1 not in row and 3 not in row else 0
        good_idxs += [str(i)] if 1 not in row and 3 not in row else []

    print nb_good
    if good_idxs: print ' '.join(good_idxs)
