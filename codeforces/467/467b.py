if __name__ == '__main__':
    n, m, k = [int(num) for num in raw_input().split()]
    armies = [int(raw_input()) for _ in range(m)]
    our_army = int(raw_input())

    num_friends = 0
    for army in armies:
        xor = army ^ our_army
        num_differ = sum(int(bit) for bit in '{0:b}'.format(xor))

        num_friends += num_differ <= k

    print num_friends
