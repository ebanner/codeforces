if __name__ == '__main__':
    n, x = [int(num) for num in raw_input().split()]

    nb_distress = 0
    for _ in range(n):
        op, d = raw_input().split()

        d = int(d)
        if op == '+':
            x += d
        else:
            assert op == '-'
            if d > x:
                nb_distress += 1
            else:
                x -= d

    print x, nb_distress
