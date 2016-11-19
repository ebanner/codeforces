import sys

if __name__ == '__main__':
    n = list(raw_input())

    if all(int(d) % 2 == 1 for d in n):
        print -1
        sys.exit()

    max_nb = rightmost_even = 0
    for i, d in enumerate(n[:-1]):
        if not int(d) % 2 == 0:
            continue

        rightmost_even = i

        if int(n[i]) < int(n[-1]):
            n[i], n[-1] = n[-1], n[i]
            break
    else:
        n[rightmost_even], n[-1] = n[-1], n[rightmost_even]

    print ''.join(n)
