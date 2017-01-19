import sys

if __name__ == '__main__':
    n = int(raw_input())
    D = [raw_input().split() for _ in range(n)]

    from_np = 0
    for d, direction in D:
        if direction in ['East', 'West']:
            if from_np in [0, 20000]:
                print 'NO'
                sys.exit()
            continue

        if direction == 'South':
            from_np = min(40000, from_np+int(d))
        else:
            from_np = max(0, from_np-int(d))

    print 'NO' if from_np else 'YES'
