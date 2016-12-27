if __name__ == '__main__':
    n, k = [int(num) for num in raw_input().split()]

    max_joy = -1 # doesn't matter what this is set to
    for i in range(n):
        f, t = [int(num) for num in raw_input().split()]
        joy = f if t <= k else f - t + k

        max_joy = max(joy, max_joy) if i > 0 else joy
        i += 1

    print max_joy
