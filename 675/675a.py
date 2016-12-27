if __name__ == '__main__':
    a, b, c = [int(num) for num in raw_input().split()]

    if c == 0:
        print 'YES' if a == b else 'NO'
    elif (b-a) / c < 0:
        print 'NO' # c is bringing you in the wrong direction
    else:
        print 'YES' if (b-a) % c == 0 else 'NO'
