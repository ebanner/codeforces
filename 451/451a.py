if __name__ == '__main__':
    n, m = [int(val) for val in raw_input().split()]

    v = min(n, m)

    print 'Malvika' if v%2 == 0 else 'Akshat'
