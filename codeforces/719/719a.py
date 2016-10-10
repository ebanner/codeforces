if __name__ == '__main__':
    n = int(raw_input())
    ms = [int(num) for num in raw_input().split()]

    if ms[-1] == 0:
        print 'UP'
    elif ms[-1] == 15:
        print 'DOWN'
    elif len(ms) == 1:
        print -1
    else:
        print {-1: 'DOWN', 1: 'UP'}[ms[-1]-ms[-2]]
