import math

if __name__ == '__main__':
    r, x, y, x_, y_ = [int(num) for num in raw_input().split()]

    d = math.sqrt((x_-x)**2 + (y-y_)**2)

    nb_pivot = d / (2*r)
    nb_pivot += 1 if not d % (2*r) == 0 else 0

    print int(nb_pivot)
