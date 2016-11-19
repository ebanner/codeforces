import sys

if __name__ == '__main__':
    n = int(raw_input())
    bits = list(raw_input())

    for i, bit in enumerate(bits):
        if bit == '0':
            break
    else:
        print n
        sys.exit()

    print i+1
