if __name__ == '__main__':
    n, m = [int(num) for num in raw_input().split()]
    G = [int(num) for num in raw_input().split()]

    nb_bus = sum(G) / m
    nb_bus += 1 if sum(G) % m else 0

    print nb_bus
