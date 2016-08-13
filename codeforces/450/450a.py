from collections import deque

if __name__ == '__main__':
    n, m = [int(num) for num in raw_input().split()]
    d = deque((i, int(num)) for i, num in enumerate(raw_input().split(), start=1))

    while len(d) > 1:
        idx, child = d.popleft()
        child -= m
        if child <= 0:
            continue

        d.append((idx, child))

    idx, _ = d.pop()

    print idx
