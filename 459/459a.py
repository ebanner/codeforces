import sys

if __name__ == '__main__':
    x1, y1, x2, y2 = [int(num) for num in raw_input().split()]

    if x1 == x2:
        width = height = abs(y1 - y2)

        x3 = x4 = x1 + width 
        y3, y4 = y1, y2

    elif y1 == y2:
        height = width = abs(x1 - x2)

        y3 = y4 = y1 + height
        x3, x4 = x1, x2

    else:
        width, height = abs(x1-x2), abs(y1-y2)
        
        try:
            assert width == height
        except AssertionError:
            print -1

            sys.exit()

        x3, y3 = x1, y2
        x4, y4 = x2, y1

    print x3, y3, x4, y4
