if __name__ == '__main__':
    n, v = [int(num) for num in raw_input().split()]

    nb_deals, sellers = 0, []
    for i in range(1, n+1):
        prices = [int(num) for num in raw_input().split()][1:]
        if v > min(prices):
            nb_deals += 1
            sellers += [str(i)]

    print nb_deals
    print ' '.join(sellers)
