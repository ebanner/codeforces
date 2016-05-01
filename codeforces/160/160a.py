def coin_generator(coin_str):
    coins = [int(coin) for coin in coin_str.split()]

    for coin in sorted(coins, reverse=True):
        yield coin


if __name__ == '__main__':
    n = int(raw_input())

    coin_str = raw_input()
    coin = coin_generator(coin_str)
    my_sum, your_sum = 0, sum(coin_generator(coin_str))
    num_coins = 0
    while True:
        if my_sum > your_sum:
            break

        my_gain = next(coin)
        my_sum += my_gain
        your_sum -= my_gain
        num_coins += 1

    print num_coins
