def ranges_generator(puzzles, n):
    for s1, s2 in zip(puzzles, puzzles[n-1:]):
        yield s2 - s1

if __name__ == '__main__':
    n, m = [int(val) for val in raw_input().split()]

    puzzles = [int(val) for val in raw_input().split()]

    puzzles = sorted(puzzles)

    ranges = list(ranges_generator(puzzles, n))

    print min(ranges)
