if __name__ == '__main__':
    s, n = [int(num) for num in raw_input().split()]
    dragons = [[int(num) for num in raw_input().split()] for _ in range(n)]

    for strength, bonus in sorted(dragons): # greedily fight weakest dragons first
        if s <= strength:
            print 'NO'

            break

        s += bonus # defeated the dragon!
    else:
        print 'YES'
