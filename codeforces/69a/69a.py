if __name__ == '__main__':
    n = int(raw_input())

    x_tot = y_tot = z_tot = 0
    for _ in range(n):
        x, y, z = [int(val) for val in raw_input().split()]

        x_tot += x
        y_tot += y
        z_tot += z

    print 'YES' if x_tot == 0 and y_tot == 0 and z_tot == 0 else 'NO'
