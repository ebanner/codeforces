import math

if __name__ == '__main__':
    t = int(raw_input())

    for _ in range(t):
        n = int(raw_input())
        sum = n*(n+1) / 2
        ceil = math.log(n, 2)
        for i in range(int(ceil) + 1):
            sum -= 2 * 2**i # multiple by 2 because we mistakenly added it

        print sum
