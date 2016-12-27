if __name__ == '__main__':
    n = int(raw_input())

    m = n / 2

    print m if n % 2 == 0 else -m - 1
