if __name__ == '__main__':
    n, m, k = [int(num) for num in raw_input().split()]
    D = [int(num) for num in raw_input().split()]

    nb_wash = 0
    for d in D:
        if d == 1:
            if m == 0:
                nb_wash += 1
                m += 1
            m -= 1
        else:
            assert d == 2
            if m == k == 0:
                nb_wash += 1
            elif k > 0:
                k -= 1
            else:
                m -= 1 # avoid using plates at all cost

    print nb_wash
