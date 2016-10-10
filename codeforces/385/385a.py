if __name__ == '__main__':
    n, c = [int(num) for num in raw_input().split()]
    nums = [int(num) for num in raw_input().split()]

    print max(max(n1-n2-c for n1, n2 in zip(nums, nums[1:])), 0)
