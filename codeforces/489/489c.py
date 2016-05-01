import operator

def do_dp(dp, cmp, init):
    M, S = len(dp)-1, len(dp[0])-1

    for m in range(2, M):
        for s in range(1, S+1):
            
            best_num = init
            for digit in range(10):
                if s-digit < 0:
                    continue

                if not dp[m-1][s-digit]:
                    continue

                num = str(digit) + dp[m-1][s-digit]
                if cmp(int(num), int(best_num)):
                    best_num = num

            dp[m][s] = str(best_num) if not best_num == init else ''

    # Last row - no leading zeros
    best_num, s, m = init, S, M
    for s in range(1, S+1):

        best_num = init
        for digit in range(1, 10):
            if s-digit < 0:
                continue

            if not dp[M-1][s-digit]:
                continue

            num = str(digit) + dp[M-1][s-digit]
            if cmp(int(num), int(best_num)):
                best_num = num

        dp[M][s] = str(best_num) if not best_num == init else ''

    return dp[M][S]


if __name__ == '__main__':
    M, S = [int(num) for num in raw_input().split()]

    # Min case
    dp = [['']*(S+1) for _ in range(M+1)]

    for i in range(S+1)[:10]:
        dp[1][i] = str(i)

    for i in range(1, M+1):
        dp[i][0] = '0'*i

    if M == 1:
        min_num = max_num = dp[1][S]
    else:
        min_num = do_dp(dp, operator.lt, init=1e100)
        max_num = do_dp(dp, operator.gt, init=0)

    if M == 1 and S == 0:
        min_num = max_num = 0
    else:
        min_num = -1 if not min_num or min_num.startswith('0') else min_num
        max_num = -1 if not max_num or max_num.startswith('0') else max_num

    print min_num, max_num
