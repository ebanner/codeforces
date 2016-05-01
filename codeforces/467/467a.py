if __name__ == '__main__':
    n = int(raw_input())

    num_accom = 0
    for _ in range(n):
        p, q = [int(val) for val in raw_input().split()]
        num_accom += 1 if q-p >= 2 else 0

    print num_accom
