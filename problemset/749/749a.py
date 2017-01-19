if __name__ == '__main__':
    k = int(raw_input())

    print k / 2

    if k % 2 == 0:
        print ' '.join('2' for _ in range(k/2))
    else:
        print ' '.join([' '.join('2' for _ in range(k/2 - 1)), '3'])
