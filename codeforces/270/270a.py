if __name__ == '__main__':
    t = int(raw_input())

    for _ in range(t):
        a = int(raw_input())

        n = 360 / float(180-a)
        if int(n) == n:
            print 'YES'
        else:
            print 'NO'
