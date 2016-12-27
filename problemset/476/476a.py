if __name__ == '__main__':
    n, m = [int(num) for num in raw_input().split()]

    # dp[i, k] is the minimum number of moves of length 1 or 2 you can take to
    # get to step i modulo k == m.
    dp = [[1e100]*m for _ in range(n+1)]

    dp[0][0] = 0
    for i in range(1, n+1):
        for k in range(m):
            #
            # You can make it to the current step with k mod m by jumping up
            # from one step below or two steps below. Both times you have to
            # have a modulo of (k-1) % m.
            #
            one_step = dp[i-1][(k-1) % m]
            two_steps = dp[i-2][(k-1) % m]

            dp[i][k] = 1 + min(one_step, two_steps)

    print int(dp[n][0]) if not dp[n][0] == 1e100 else -1
