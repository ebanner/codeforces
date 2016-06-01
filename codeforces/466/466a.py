import sys


def do_compute(n, m, a, b):
    if not b/float(m) < a:
        return n*a # more expensive *per day* for the multi-day pass

    # Cheaper *per day* for the multi-day pass

    cost = (n/m)*b
    if n % m:
        rest = min((n%m)*a, b)
        cost += rest

    return cost

if __name__ == '__main__':
    n, m, a, b = [int(num) for num in raw_input().split()]

    min_cost = do_compute(n, m, a, b)

    print min_cost
