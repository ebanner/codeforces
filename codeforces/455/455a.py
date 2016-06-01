from collections import defaultdict

MAX_NUM = 10**5


if __name__ == '__main__':
    n = int(raw_input())
    seq = [int(num) for num in raw_input().split()]

    # dp[i] is the maximum score you can get by only considering elements of seq
    # which are less than or equal to i.
    #
    dp = [0]*(MAX_NUM+1)

    freq = defaultdict(int)
    for a in seq:
        freq[a] += 1

    dp[0], dp[1] = 0, freq[1]
    for i in range(2, MAX_NUM+1):
        take_it = i*freq[i] + dp[i-2]
        dont_take = dp[i-1]

        dp[i] = max(take_it, dont_take)

    print dp[-1]
