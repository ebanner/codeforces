if __name__ == '__main__':
    x1, y1 = [int(num) for num in raw_input().split()]
    x2, y2 = [int(num) for num in raw_input().split()]

    dx, dy = abs(x1-x2), abs(y1-y2)

    if dx == 0:
        print dy
    elif dy == 0:
        print dx
    else:
        m = min(dx, dy)
        print m + dx-m + dy-m
