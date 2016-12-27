if __name__ == '__main__':
    n, l = [int(num) for num in raw_input().split()]
    lantern_locs = [int(num) for num in raw_input().split()]

    lantern_locs = sorted(lantern_locs)

    d = lantern_locs[0]
    for l1, l2 in zip(lantern_locs, lantern_locs[1:]):
        d = max(d, (l2-l1) / 2.)
    d = max(d, l-lantern_locs[-1])

    print d
