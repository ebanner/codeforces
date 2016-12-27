from collections import defaultdict

if __name__ == '__main__':
    nums = [int(num) for num in raw_input().split()]

    d = defaultdict(int)
    for num in nums:
        d[num] += 1

    d = {k: min(v, 3) for k, v in d.items() if v >= 2}
    d = {k: v for k, v in d.items() if v >= 2}
    d = {k: k*v for k, v in d.items()}

    print sum(nums) - max(d.values() if d else [0])
