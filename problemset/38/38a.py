if __name__ == '__main__':
    n = int(raw_input())
    D = [int(num) for num in raw_input().split()]
    a, b = [int(num)-1 for num in raw_input().split()]

    print sum(D[a:b])
