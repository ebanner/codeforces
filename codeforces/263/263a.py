def find_one():
    for i in range(1, 6):
        row = [int(bit) for bit in raw_input().split()]
        for j, k in enumerate(row, start=1):
            if k:
                return (i, j)


if __name__ == '__main__':
    i, j = find_one()

    print abs(i-3) + abs(j-3)
