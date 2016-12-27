if __name__ == '__main__':
    n, k = [int(num) for num in raw_input().split()]
    nums = raw_input().split()

    nb_nums = 0
    for num in nums:
        nb_lucky = sum(1 for d in num if d in '47')
        if nb_lucky <= k:
            nb_nums += 1

    print nb_nums
