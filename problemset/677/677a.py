if __name__ == '__main__':
    n, h = [int(num) for num in raw_input().split()]
    heights = [int(num) for num in raw_input().split()]

    nb_tall = sum(1 for height in heights if height > h)

    print 2*nb_tall + n-nb_tall
