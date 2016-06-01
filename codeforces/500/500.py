if __name__ == '__main__':
    n, t = [int(num) for num in raw_input().split()]

    portals = [int(num) for num in raw_input().split()]

    i, t = 0, t-1
    while True:
        if i == t:
            print 'YES'
            break
        elif i > t-1:
            print 'NO'
            break
        else:
            i += portals[i]
