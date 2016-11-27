if __name__ == '__main__':
    n, m = [int(num) for num in raw_input().split()]
    pairs = [[int(num)-1 for num in raw_input().split()] for _ in range(m)]

    rows, cols = [1]*n, [1]*n
    nb_row = nb_col = n
    nb_free, frees = n**2, []
    for r, c in pairs:
        if rows[r]:
            nb_free -= nb_col
            rows[r] = 0
            nb_row -= 1
        if cols[c]:
            nb_free -= nb_row
            cols[c] = 0
            nb_col -= 1

        frees.append(nb_free)

    print ' '.join(str(free) for free in frees)
