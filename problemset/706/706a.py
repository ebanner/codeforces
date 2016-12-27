import math

if __name__ == '__main__':
    x_, y_ = [int(num) for num in raw_input().split()]
    n = int(raw_input())

    min_time = 400 # no way the time will exceed 400
    for _ in range(n):
        x, y, v = [int(num) for num in raw_input().split()]

        # zero-center location
        x -= x_
        y -= y_

        # compute radius
        z = math.sqrt(x**2 + y**2)

        t = z / v
        min_time = min(min_time, t)

    print min_time
