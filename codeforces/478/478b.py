import math

import heapq


def num_pairs(group_size):
    return (group_size*(group_size-1)) / 2


if __name__ == '__main__':
    m, n = [int(num) for num in raw_input().split()]

    max_team_size = m - n + 1
    max_num_friends = (max_team_size*(max_team_size-1)) / 2

    min_team_size = m / float(n)
    
    # Compute both possibilities
    p, q = math.floor(min_team_size), math.ceil(min_team_size)

    if p == min_team_size:
        min_num_friends = n*num_pairs(p)
    else:
        h_min = [p]*(n-1) # initialize min heap
        leftover = m - (n-1)*p
        heappush(h_min, leftover)

        h_max = [-p]*(n-1) # initialize max heap
        heappush(h_max, leftover)

        # Attempt to take one member out of the largest team and add it to the
        # smallest team. Repeat until fixed point is reached.


    print int(min_num_friends), max_num_friends
