if __name__ == '__main__':
    n = int(raw_input())

    n_  = n % 4
    n__ = n % 2

    one   = {0: 1, 1: 1}
    two   = {0: 1, 1: 2, 2: 4, 3: 3}
    three = {0: 1, 1: 3, 2: 4, 3: 2}
    four  = {0: 1, 1: 4}

    print (one[n__] + two[n_] + three[n_] + four[n__]) % 5
