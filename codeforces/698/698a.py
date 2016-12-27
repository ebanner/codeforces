# TODO
#
# - [ ] DP
#   - [ ] Forward
#   - [ ] Backward
# - [X] Memoization
# - [X] BFS solution
#
# NOTES
#
# Actually, recursion itself isn't even necessarily right to left. In fact we
# should be thinking of it as starting at one step in the tree and using that
# result to compute the next one to the right. So that unifies all of these
# approaches as building a tree from left to right.
#
# Hmm, I'll actually have to think about that a little bit more. I've always
# thought of recursion as "OK we're interested in computing F(n). How can we use
# F(n-1) to do that?" Not "OK we have F(n-1). How can we use it to compute
# F(n)?" Indeed, during Jaime and Arnav's lectures on DP, they very much used a
# "F(n) in terms of F(n-1)" approach. The "F(n-1) to F(n)" corresponds more
# naturally to induction.
#
# Take fibonnaci for example. If you started thinking in terms of "How can I
# use F(n-1) to compute F(n)?" Well you would have to say "I also need F(n-2).
# Then I could use them both to compute F(n)." But perhaps this is more
# cumbersome than saying "I have F(n). I know by definition that it *is* F(n-2)
# and F(n-1)." In this sense, it is definitional. The left-to-right approach is
# more constructivist in its nature. This is perhaps useful for DP.
#
# Although DP can still be viewed as successive right-to-left operations (e.g.
# F(2) in terms of F(1), then F(3) in terms of F(2), and so on). In this case,
# we are just applying repeated definitions of the recursion rule. As opposed to
# having F(1), then using it to compute (or "construct") F(2), then using F(2)
# to construct F(3). In this sense we are going forward and it /feels/ more
# natural, though less general somehow.
#

def memoize(f):
    d = {}
    def wrapper(*args):
        if args not in d:
            d[args] = f(*args)
        return d[args]
    return wrapper

def min_rest(T, A):
    """Minimum days to rest at time `T` given agenda `A`

    Parameters
    ----------
    T : day
    A : list of options for every day

    """
    @memoize
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

def bfs_solve(A, n):
    """Breadth-first search solution
    
    State
    -----
    t : time step
    activity : activity @ time `t`
    nb_rest : number of rests taken

    Variables
    ---------
    Q : bfs queue
    R : nb_activity x n table where R[i][j] = minimum number of rests for path
        ending in activity i @ timestep j found so far

    """
    from collections import deque

    Q = deque()
    for activity in A[0]:
        Q.append([0, activity, 1 if activity == REST else 0])

    R = [[1e100]*n for _ in range(3)]
    for activity in A[0]:
        R[activity][0] = 1 if activity == REST else 0

    # for r in R:
    #     print r
    # print

    while Q:
        t, activity, nb_rest = Q.popleft()
        # print 'popped t={}, {}, nb_rest={}'.format(t, N[activity], nb_rest)

        if t == n-1:
            # print 'done, t == n'
            # print
            continue # don't add more neighbors

        if nb_rest > R[activity][t]:
            # print 'better node added in the meantime'
            # print
            continue # better node may have been added in the mean time

        # Add neighbors
        for tomorrow_activity in A[t+1]:
            if activity == tomorrow_activity and activity in [CONTEST, GYM]:
                continue # no repeats

            tomorrow_rest = nb_rest
            tomorrow_rest += 1 if tomorrow_activity == REST else 0
            if tomorrow_rest >= R[tomorrow_activity][t+1]:
                continue # already found as good or better path

            # print 'adding t={}, {}, nb_rest={}'.format(t+1, N[tomorrow_activity], tomorrow_rest)
            R[tomorrow_activity][t+1] = tomorrow_rest
            Q.append([t+1, tomorrow_activity, tomorrow_rest]) # path checks out

        # for r in R:
        #     print r
        # print

    return min(R[i][n-1] for i in range(3))

if __name__ == '__main__':
    n = int(raw_input())
    A = [int(num) for num in raw_input().split()]

    REST, CONTEST, GYM = range(3)
    N = {0: 'REST', 1: 'CONTEST', 2: 'GYM'}
    D = {0: {REST},
         1: {CONTEST, REST},
         2: {GYM, REST},
         3: {CONTEST, GYM, REST}}

    print bfs_solve(A=[D[a] for a in A], n=n)

    # if n == 1:
    #     print 1 if A[0] == REST else 0
    # else:
    #     print min_rest(T=n, A=[None]+[D[a] for a in A]) # one-indexed
