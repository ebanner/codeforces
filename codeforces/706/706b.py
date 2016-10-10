def bs(X, a):
    """Binary search `X` for `a`

    Parameters
    ----------
    X : sorted collection
    a : value being searched for

    Return the greatest index in X whose value is less than or equal to `a`. Add
    1 to this number so we can interpret it as the number of numbers less than
    or equal to `a`.

    """
    lo, hi = 0, len(X)-1

    highest_idx = 0
    while lo <= hi:
        mid = (lo+hi) / 2
        if X[mid] == a:
            return mid + 1

        if a < X[mid]:
            hi = mid - 1
        else:
            assert X[mid] < a
            highest_idx = mid + 1
            lo = mid + 1

    return highest_idx

if __name__ == '__main__':
    n = int(raw_input())
    prices = sorted(int(num) for num in raw_input().split())
    q = int(raw_input())

    for _ in range(q):
        m = int(raw_input())
        print bs(prices, m)
