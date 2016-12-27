if __name__ == '__main__':
    n, k = [int(val) for val in raw_input().split()]
    costs = [int(val) for val in raw_input().split()]

    # Greedily pick instruments which take smallest time to learn
    cost = iter(sorted((v, i) for (i, v) in enumerate(costs)))

    cost_allowance, instruments = k, []
    while True:
        try:
            proposed_cost, i = next(cost)
        except StopIteration:
            break

        if cost_allowance-proposed_cost < 0:
            break # can't afford it

        # Can afford it - commit to learning it
        instruments.append(i)
        cost_allowance -= proposed_cost

    print len(instruments)
    if instruments:
        print ' '.join(str(instrument+1) for instrument in instruments)
