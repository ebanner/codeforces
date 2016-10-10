if __name__ == '__main__':
    n = int(raw_input())
    nums = [int(num) for num in raw_input().split()]

    max_diff = max(b-a for a, b in zip(nums, nums[1:]))
    min_diff = min(nums[i+1]-nums[i-1] for i in range(1, n-1))

    print max(max_diff, min_diff)
