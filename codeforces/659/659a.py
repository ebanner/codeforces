if __name__ == '__main__':
    n, a, b = [int(num) for num in raw_input().split()]

    print ((a+b) % n) or n
