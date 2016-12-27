if __name__ == '__main__':
    k, n, w = [int(val) for val in raw_input().split()]

    cost = k * w*(w+1)/2

    print max(cost-n, 0)
