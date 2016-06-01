import sys

if __name__ == '__main__':
    coins = [int(num) for num in raw_input().split()]

    if sum(coins) == 0:
        print -1

        sys.exit()

    init = sum(coins) / 5.
    print int(init) if int(init) == init else -1
