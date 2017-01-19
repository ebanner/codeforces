if __name__ == '__main__':
    n, k = [int(num) for num in raw_input().split()]

    remaining_time = 240 - k
    i = 0 # start on first problem
    while True:
        if 5*i > remaining_time or i > n:
            break

        remaining_time -= 5*i # do the problem
        i += 1 # turn the page

    print i - 1
