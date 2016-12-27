if __name__ == '__main__':
    n = int(raw_input())
    times = [[int(num) for num in raw_input().split()] for _ in range(n)]

    chain = max_chain = 1
    for (h1, m1), (h2, m2) in zip(times, times[1:]):
        chain = chain+1 if h2 == h1 and m2 == m1 else 1
        max_chain = max(chain, max_chain)

    print max_chain
