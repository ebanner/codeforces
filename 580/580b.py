if __name__ == '__main__':
    n, d = [int(num) for num in raw_input().split()]
    pairs = sorted([[int(num) for num in raw_input().split()] for _ in range(n)])

    M, S = zip(*pairs)

    left_idx = right_idx = 0
    friendship_sum = max_friendship = S[0]
    while True:
        right_idx += 1
        if right_idx == n:
            break

        friendship_sum += S[right_idx]
        while M[right_idx] - M[left_idx] > d:
            friendship_sum -= S[left_idx]
            left_idx += 1

        # Valid arrangement
        max_friendship = max(friendship_sum, max_friendship)

    print max_friendship
