if __name__ == '__main__':
    n = int(raw_input())
    nums = [int(num) for num in raw_input().split()]

    rems = [0, 0]
    for mod in (num % 2 for num in nums[:3]):
        rems[mod] += 1

    bit = 0 if rems[0] > rems[1] else 1 # majority vote
    for i, num in enumerate(nums):
        if not num % 2 == bit:
            print i + 1

            break
