if __name__ == '__main__':
    n, m = [int(num) for num in raw_input().split()]

    a2b = {}
    for _ in range(m):
        a, b = raw_input().split()
        a2b[a] = b

    lecture = raw_input().split()

    b2a = {b: a for a, b in a2b.items()}

    print ' '.join(word if len(word) <= len(a2b[word]) else a2b[word] for word in lecture)
