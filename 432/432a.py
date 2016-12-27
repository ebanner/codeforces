if __name__ == '__main__':
    n, k = [int(num) for num in raw_input().split()]
    exp_lvls = [int(num) for num in raw_input().split()]

    exps = [0]*(n+1)
    for exp in exp_lvls:
        exps[exp] += 1

    print sum(exps[:5-k+1]) / 3
