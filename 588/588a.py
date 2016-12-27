if __name__ == '__main__':
    n = int(raw_input())

    needs, prices = zip(*[map(lambda s: int(s), raw_input().split()) for _ in range(n)])

    i = cost = 0
    while i < n:
        need, price = needs[i], prices[i]

        # How many days until a cheaper price?
        num_stock = need
        i += 1
        while i < n and prices[i] > price:
            num_stock += needs[i] # keep stocking up until you hit a day which is cheaper to buy
            i += 1

        # price is finally higher - cost incurred
        cost += price * num_stock

    print cost
