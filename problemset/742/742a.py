if __name__ == '__main__':
    n = int(raw_input())

    if n == 0:
        print 1
    else:
        print {0: 6, 1: 8, 2: 4, 3: 2}[n%4]
