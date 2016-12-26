if __name__ == '__main__':
    n, t = [int(num) for num in raw_input().split()]
    A = [int(num) for num in raw_input().split()]

    i = j = 0
    running_total = max_book = 0
    while j < n:
        j += 1
        running_total += A[j-1] # try to step j

        while running_total > t and i < j:
            running_total -= A[i]
            i += 1 # fixup i

        if i == j:
            continue

        max_book = max(j-i, max_book)

    print max_book
