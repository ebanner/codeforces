if __name__ == '__main__':
    k2, k3, k5, k6 = [int(num) for num in raw_input().split()]

    nb256 = min(k2, k5, k6)
    k2, k5, k6 = k2-nb256, k5-nb256, k6-nb256

    nb32 = min(k3, k2)

    print nb256*256 + nb32*32
