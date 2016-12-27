# dynamic programming approach:
#
#   - let pi(a, b) be the maximum number of timesteps that both controllers will
#     remain charged.
#   - we have the following:
#     - pi(i, 0) = pi(0, j) = pi(1, 1) = 0 for all i, j
#     - pi(i, j) = max(
#                      pi(i+1, j-2), # charge the first
#                      pi(i-2, j+1)  # charge the second
#                  )

if __name__ == '__main__':
    a, b = [int(num) for num in raw_input().split()]

    # build base cases
    pi = [[-1]*101 for _ in range(101)]
    for i in range(101):
        pi[i][0] = pi[0][i] = 0
    pi[1][1] = 0

    for i in range(1, 101):
        for j in range(1, 101):
