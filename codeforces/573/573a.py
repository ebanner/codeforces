if __name__ == '__main__':
    n = int(raw_input())
    nums = [int(num) for num in raw_input().split()]

    for i, num in enumerate(nums):
        while num % 3 == 0:
            num /= 3
        while num % 2 == 0:
            num /= 2

        nums[i] = num

    print 'Yes' if all(num == nums[0] for num in nums) else 'No'
