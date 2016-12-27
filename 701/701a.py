if __name__ == '__main__':
    n = int(raw_input())
    nums = [int(num) for num in raw_input().split()]

    nums = sorted((num, i+1) for i, num in enumerate(nums)) # 1-based indexing
    idxs = [i for num, i in nums]

    for i in range(n/2):
        print idxs[i], idxs[-(i+1)]
