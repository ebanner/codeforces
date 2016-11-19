if __name__ == '__main__':
    n = int(raw_input())
    grid = [raw_input() for _ in range(n)]

    x_color, fill_color = grid[0][0], grid[0][1]
    try:
        for i in range(n):
            for j in range(n):
                if i == j or i + j == n-1:
                    assert grid[i][j] == x_color
                else:
                    assert grid[i][j] == fill_color
    except:
        print 'NO'
    else:
        print 'YES' if not x_color == fill_color else 'NO'
