import sys

if __name__ == '__main__':
    n, m = [int(num) for num in raw_input().split()]

    for _ in range(n):
        for color in raw_input().split():
            if color == 'C' or color == 'M' or color == 'Y':
                print '#Color'
                sys.exit()

    print '#Black&White'
