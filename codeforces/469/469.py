if __name__ == '__main__':
    n = int(raw_input())

    ps = [int(num) for num in raw_input().split()]
    qs = [int(num) for num in raw_input().split()]

    p, ps = ps[0], ps[1:]
    q, qs = qs[0], qs[1:]

    print 'I become the guy.' if len(set(ps+qs)) == n else 'Oh, my keyboard!'
