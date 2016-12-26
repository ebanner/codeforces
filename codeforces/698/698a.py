def min_rest(T, A):
    """Minimum days to rest at time `T` given agenda `A`

    Parameters
    ----------
    T : day
    A : list of options for every day

    """
    def rest_recursive(t, today_activity, depth=0):
        """Minimum days of rest ending in today's activity

        Parameters
        ----------
        t : day
        today_activity : either CONTEST, GYM, or REST

        Delete gym or contest from yesterday's activities if today's activity is
        either CONTEST or GYM.

        """
        # print '{}rest_recursive(t={}, today_activity={}'.format(' '*depth, t, N[today_activity])
        if t == 1:
            min_rest = 1 if today_activity == REST else 0
            # print '{}found min_rest={} for t={}, today_activity={}'.format(' '*depth, min_rest, t, N[today_activity])
            return min_rest

        min_rest = 1e100
        for yesterday_activity in A[t-1]:
            if today_activity == yesterday_activity and today_activity in [GYM, CONTEST]:
                continue

            nb_rest = rest_recursive(t-1, yesterday_activity, depth+4)
            nb_rest += 1 if today_activity == REST else 0
            min_rest = min(nb_rest, min_rest)

        # print '{}found min_rest={} for t={}, today_activity={}'.format(' '*depth, min_rest, t, N[today_activity])
        return min_rest

    min_rest = 1e100
    for today_activity in A[-1]:
        for yesterday_activity in A[T-1]:
            if today_activity == yesterday_activity and today_activity in [GYM, CONTEST]:
                continue

            nb_rest = rest_recursive(T-1, yesterday_activity)
            nb_rest += 1 if today_activity == REST else 0
            min_rest = min(nb_rest, min_rest)

    return min_rest

if __name__ == '__main__':
    n = int(raw_input())
    A = [int(num) for num in raw_input().split()]

    REST, CONTEST, GYM = range(3)
    N = {0: 'REST', 1: 'CONTEST', 2: 'GYM'}
    D = {0: {REST},
         1: {CONTEST, REST},
         2: {GYM, REST},
         3: {CONTEST, GYM, REST}}

    if n == 1:
        print 1 if A[0] == REST else 0
    else:
        print min_rest(T=n, A=[None]+[D[a] for a in A]) # one-indexed
