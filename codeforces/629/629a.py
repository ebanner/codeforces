if __name__ == '__main__':
    n = int(raw_input())
    cake = [list(raw_input()) for _ in range(n)]
    cake = [[{'.': 0, 'C': 1}[square] for square in row] for row in cake]

    rows = [sum(row) for row in cake]
    cols = [0]*n
    for i, row in enumerate(cake):
        for j, elem in enumerate(row):
            cols[j] += elem

    nb_pair = 0
    nb_pair += sum(nb_elem*(nb_elem-1)/2 for nb_elem in rows)
    nb_pair += sum(nb_elem*(nb_elem-1)/2 for nb_elem in cols)

    print nb_pair
