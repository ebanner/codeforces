if __name__ == '__main__':
    n = raw_input()

    n = n.replace('4', '0').replace('7', '1')
    nb_bits = len(n)

    total = sum(2**i for i in range(1, nb_bits))
    total += int(n, 2) + 1

    print total
