if __name__ == '__main__':
    n, a, b = [int(num) for num in raw_input().split()]

    num_pos = 0
    for p in range(n):
        if p-b <= 0 and p+a <= n-1:
            num_pos += 1
        else:
            break

    print num_pos
