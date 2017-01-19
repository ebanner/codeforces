from collections import defaultdict

if __name__ == '__main__':
    n = int(raw_input())
    T = [raw_input() for _ in range(n)]

    G = defaultdict(int)
    for t in T:
        G[t] += 1

    print sorted(((v, k) for k, v in G.items()), reverse=True)[0][1]
