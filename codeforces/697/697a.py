if __name__ == '__main__':
    t, s, x = [int(num) for num in raw_input().split()]

    k1, k2 = (x-t) / float(s), (x-t-1) / float(s)

    if k1 == int(k1) and k1 >= 0:
        print 'YES'
    elif k2 == int(k2) and k2 > 0:
        print 'YES'
    else:
        print 'NO'
