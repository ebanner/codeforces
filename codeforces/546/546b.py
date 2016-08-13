if __name__ == '__main__':
    n = int(raw_input())
    scores = [int(num) for num in raw_input().split()]

    freqs = [0]*(n+1)
    for score in scores:
        freqs[score] += 1

    cost = carry = 0
    for i in range(1, n+1):
        freqs[i] += carry
        carry = 0
        carry = max(freqs[i]-1, 0)
        freqs[i] = freqs[i] - carry
        cost += carry

    print cost
