if __name__ == '__main__':
    a, b = [int(num) for num in raw_input().split()]

    min_num = min(a, b)
    a -= min_num
    b -= min_num

    print min_num, a/2 + b/2
