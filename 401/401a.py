if __name__ == '__main__':
    n, x = [int(num) for num in raw_input().split()]
    total = sum(int(num) for num in raw_input().split())

    nb_cards = abs(total) / x
    nb_cards += 1 if total % x else 0

    print nb_cards
