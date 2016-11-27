if __name__ == '__main__':
    n, m = [int(num) for num in raw_input().split()]

    grid = [raw_input() for _ in range(n)]

    ds = [(0, 0), (1, 0), (0, 1), (1, 1)]
    face, nb_face = {'f', 'a', 'c', 'e'}, 0
    for i in range(n-1):
        for j in range(m-1):
            chars = set(grid[i+di][j+dj] for di, dj in ds)
            if chars == face:
                nb_face += 1

    print nb_face
