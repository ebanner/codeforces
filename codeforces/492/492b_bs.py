# binary search implementation - fails on the third test case for some reason

def covered(l, d, lantern_locs):
    """Do lanterns light up street?
    
    Concretely, this function returns True if lanterns at `lantern_locs` each
    with light radius `d` light up a street of length `l` and False otherwise.
    
    """
    pos = 0

    for lantern_loc in lantern_locs:
        if lantern_loc-d > pos:
            return False # light does not extend far enough

        pos = lantern_loc + d

        if pos >= l:
            return True # made it to the end!


if __name__ == '__main__':
    n, l = [int(num) for num in raw_input().split()]
    lantern_locs = sorted(int(num) for num in raw_input().split())

    lo, hi = 0., float(n) # lantern radii
    while True:
        mid = (lo+hi) / 2

        if hi-lo < 1e-9:
            print mid
            break

        if covered(l, mid, lantern_locs):
            hi = mid
        else:
            lo = mid
