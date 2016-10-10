if __name__ == '__main__':
    nums = sorted(int(num) for num in raw_input().split())

    print nums[2]-nums[1] + nums[1]-nums[0]
