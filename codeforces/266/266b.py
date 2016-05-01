def swap_generator(line):
    """Yield all tuples (i,j) where line[i] == 'B' and line[j] == 'G'

    j = i+1 always!

    """
    line = line[:]

    for i in range(len(line)-1):
        if line[i] == 'B' and line[i+1] == 'G':
            yield i, i+1

if __name__ == '__main__':
    n, t = [int(val) for val in raw_input().split()]

    line = list(raw_input())

    for _ in range(t):
        for i, j in swap_generator(line):
            line[i], line[j] = line[j], line[i]

    print ''.join(line)
