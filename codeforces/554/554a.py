if __name__ == '__main__':
    s = raw_input()

    k = len(s)
    l = 26 - k

    prod = 1
    for i in range(k+1):
        prod *= l-i
