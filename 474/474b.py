if __name__ == '__main__':
    n = int(raw_input())
    num_worms_piles = [int(num) for num in raw_input().split()]
    num_juicy = int(raw_input())
    labels_juicy = [int(num)-1 for num in raw_input().split()]

    piles = [0]*1000000

    i = j = 0
    for num_worms in num_worms_piles:
        for k in range(num_worms):
            piles[i] = j
            i += 1

        j += 1

    for label_juicy in labels_juicy:
        print piles[label_juicy]+1
