if __name__ == '__main__':
    n = int(raw_input())
    bits = [int(num) for num in raw_input().split()]

    max_sum = 0
    for i in range(n):
        for j in range(i+1, n+1):
            max_sum = max(sum(bits[:i] + [1-bit for bit in bits[i:j]] + bits[j:]), max_sum)

    print max_sum
