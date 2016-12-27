if __name__ == '__main__':
    n, k, l, c, d, p, nl, np = [int(num) for num in raw_input().split()]

    a = k*l / nl
    aa = c*d
    aaa = p / np

    print min(a, aa, aaa) / n
