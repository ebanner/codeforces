import math

if __name__ == '__main__':
    x = int(raw_input())

    print sum(1 for bit in '{0:b}'.format(x) if bit == '1')
