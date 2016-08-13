if __name__ == '__main__':
    n, m = [int(num) for num in raw_input().split()]
    bulbs = [0]*m

    for _ in range(n):
        for i in raw_input().split()[1:]:
            bulbs[int(i)-1] = 1

    print 'YES' if all(bulbs) else 'NO'
