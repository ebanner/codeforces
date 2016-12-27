if __name__ == '__main__':
    n = int(raw_input())
    skills = [int(num) for num in raw_input().split()]

    sorted_tups = sorted([(v, i) for i, v in enumerate(skills)], reverse=True)

    values, idxs = zip(*sorted_tups)

    ratings = range(n)
    for i in range(1, n):
        if values[i] == values[i-1]:
            ratings[i] = ratings[i-1]

    orig_ratings = [0]*n
    for i, idx in enumerate(idxs):
        orig_ratings[idx] = ratings[i]

    print ' '.join(str(orig_rating+1) for orig_rating in orig_ratings)
