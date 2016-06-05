import math

if __name__ == '__main__':
    n, x = [int(num) for num in raw_input().split()]

    # factorize x
    num_x = 0
    for factor in range(1, int(math.floor(math.sqrt(x)))+1):
        k, l = factor, x/factor

        if x % factor == 0 and k <= n and l <= n:
            num_x += 2 if k != l else 1

    print num_x
