if __name__ == '__main__':
    n = int(raw_input())
    mins, maxes = zip(*([int(num) for num in raw_input().split()] for _ in range(3)))
    mins, maxes = list(mins), list(maxes)

    # Get minimum number of diplomas out of the way
    nb_given = [0, 0, 0]
    for i in range(3):
        n -= mins[i]
        nb_given[i] += mins[i]
        maxes[i] -= mins[i]
        mins[i] -= mins[i]

    priority_idx = min(i for i, max in enumerate(maxes) if max > 0)
    print priority_idx
    print n
    while n > 0:
        n -= 1
        maxes[priority_idx] -= 1
        nb_given[i] += 1

        if maxes[priority_idx] == 0:
            priority_idx += 1
            if maxes[priority_idx] == 0:
                priority_idx += 1

    print nb_given
