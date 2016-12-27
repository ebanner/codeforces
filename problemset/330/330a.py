def make_cake(nb_row, nb_col):
    cake = [[0]*nb_col for _ in range(nb_row)]

    for i in range(nb_row):
        row = raw_input()
        for j, cell in enumerate(row):
            cake[i][j] = 1 if cell == '.' else 0

    return cake

if __name__ == '__main__':
    nb_row, nb_col = [int(num) for num in raw_input().split()]

    cake = make_cake(nb_row, nb_col)

    edible_rows, edible_cols = [1]*nb_row, [1]*nb_col
    for i in range(nb_row):
        for j in range(nb_col):
            edible_rows[i] &= cake[i][j]
            edible_cols[j] &= cake[i][j]

    edible_rows = [i for i, edible in enumerate(edible_rows) if edible]
    edible_cols = [i for i, edible in enumerate(edible_cols) if edible]

    nb_eat = 0
    for i in edible_rows:
        for j in range(nb_col):
            nb_eat += not cake[i][j] == -1
            cake[i][j] = -1

    for j in edible_cols:
        for i in range(nb_row):
            nb_eat += not cake[i][j] == -1
            cake[i][j] = -1

    print nb_eat
