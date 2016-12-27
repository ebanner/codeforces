import sys

if __name__ == '__main__':
    n = int(raw_input())
    nums = [int(num) for num in raw_input().split()]

    S = sum(nums)
    if not S % 3 == 0:
        print 0
        sys.exit()

    # Create array is_suffix[i] = True if sum(nums[i:n]) == S/3
    is_suffix, total = [False]*n, 0
    for i in reversed(range(n)):
        total += nums[i]
        if total == S/3:
            is_suffix[i] = True

    # Create array `nb_suffix` where nb_suffix[i] == the number of suffixes from
    # i..n that sum up to S/3
    nb_suffix, total = [0]*n, 0
    for i in reversed(range(n)):
        total += is_suffix[i]
        nb_suffix[i] = total

    total = nb_partition = 0
    for i in range(n-2):
        total += nums[i]
        if total == S/3:
            nb_partition += nb_suffix[i+2]

    print nb_partition
