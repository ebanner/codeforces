if __name__ == '__main__':
    n = int(raw_input()) - 1
    nums = [int(num)-1 for num in raw_input().split()]

    # find which guy is closer to an edge
    lodx, hidx = nums.index(0), nums.index(n)
    lo_dist, hi_dist = min(lodx, abs(n-lodx)), min(hidx, abs(n-hidx))

    if lo_dist > hi_dist:
        lodx = n if hidx < abs(n-hidx) else 0
    else:
        assert lo_dist <= hi_dist
        hidx = n if lodx < abs(n-lodx) else 0

    print abs(lodx-hidx)
