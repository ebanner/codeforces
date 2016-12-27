if __name__ == '__main__':
    n = int(raw_input())

    nb_digit, i = range(2)
    while 10**i - 1 < n:
        nb_num = 10**i - 10**(i-1)
        num_length = i

        nb_digit += nb_num*num_length

        i += 1

    i -= 1
    nb_num = n - 10**i + 1
    num_length = i + 1
    nb_digit += nb_num*num_length

    print nb_digit
