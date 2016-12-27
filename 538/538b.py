if __name__ == '__main__':
    n = [int(digit) for digit in raw_input()]

    quasis = []
    while any(n):
        scratch = [d and 1 for d in n]
        quasis.append(''.join(str(d) for d in scratch))
        for i, d in enumerate(scratch):
            n[i] -= d

    print len(quasis)
    print ' '.join(quasi.lstrip('0') for quasi in quasis)
