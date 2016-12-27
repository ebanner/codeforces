if __name__ == '__main__':
    n = int(raw_input())
    beauties = [int(beauty_num) for beauty_num in raw_input().split()]

    min_beauty, max_beauty = min(beauties), max(beauties)

    min_beauties = sum(1 for beauty in beauties if beauty == min_beauty)
    max_beauties = sum(1 for beauty in beauties if beauty == max_beauty)

    if min_beauty == max_beauty:
        numer = min_beauties*(min_beauties-1)
        combs = numer / 2
    else:
        combs = min_beauties*max_beauties 

    print max_beauty-min_beauty, combs
