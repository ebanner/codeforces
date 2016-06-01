if __name__ == '__main__':
    n = int(raw_input())

    nums = [i for i in range(100)]

    accum = 0
    for i in range(100):
        accum += nums[i]
        nums[i] = accum

    accum = 0
    for i in range(100):
        accum += nums[i]
        nums[i] = accum

    i = 0
    while True:
        if nums[i] > n:
            print i-1

            break

        i += 1
