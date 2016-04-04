import math


if __name__ == '__main__':
    n, m, a = raw_input().split()
    n, m, a = [int(val) for val in (n, m, a)]

    vert = math.ceil(n / float(a))
    horiz = math.ceil(m / float(a))

    print int(vert) * int(horiz)
