if __name__ == '__main__':
    n, m = [int(num) for num in raw_input().split()]

    nb_pair = 0
    for i in range(1, n+1):
        nb_pair += m / 5
        nb_pair += m%5 >= 5-(i%5)

    print nb_pair
