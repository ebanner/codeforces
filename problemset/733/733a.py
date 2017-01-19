V = {'A', 'E', 'I', 'O', 'U', 'Y'}

if __name__ == '__main__':
    C = raw_input()
    n = len(C)

    B = [1 if c in V else 0 for c in C]
    I = [i for i, b in enumerate(B) if b == 1]
    D = [i2 - i1 for i1, i2 in zip(I, I[1:])]

    print max(I[0]+1, max(D) if D else 0, n-I[-1])
