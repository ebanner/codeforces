if __name__ == '__main__':
    x = int(raw_input())

    if not x % 2 == 0:
        print 0
    else:
        print x/4 - 1 if x % 4 == 0 else x/4
