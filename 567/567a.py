if __name__ == '__main__':
    n = int(raw_input())
    locs = [int(num) for num in raw_input().split()]

    mins, maxes = [0]*n, [0]*n
    for i, loc in enumerate(locs[1:-1], start=1):
        mins[i] = min(loc-locs[i-1], locs[i+1]-loc)
        maxes[i] = max(loc-locs[0], locs[-1]-loc)

    mins[0], maxes[0] = locs[1]-locs[0], locs[-1]-locs[0]
    mins[-1], maxes[-1] = locs[-1]-locs[-2], locs[-1]-locs[0]

    for min, max in zip(mins, maxes):
        print min, max
