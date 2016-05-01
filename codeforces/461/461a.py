import heapq
from heapq import heappush, heappop

if __name__ == '__main__':
    n = int(raw_input())
    nums = [int(num) for num in raw_input().split()]

    group2 = []
    for num in nums:
        heappush(group2, num)

    group1, total = {}, 0
    while True:
        total += sum(group1) + sum(group2) # add

        min_elem = heappop(group2) # split
        if not group2:
            break
        else:
            group1 = [min_elem]

    print total
