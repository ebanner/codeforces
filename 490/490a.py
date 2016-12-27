if __name__ == '__main__':
    n = int(raw_input())
    traits = [int(num)-1 for num in raw_input().split()]

    skills, idxs = [0]*3, [[] for _ in range(3)]
    for i, trait in enumerate(traits):
        skills[trait] += 1
        idxs[trait] += [i]

    num_teams = min(skills)
    print num_teams

    for i in range(num_teams):
        print ' '.join(str(idxs[j][i]+1) for j in range(3))
