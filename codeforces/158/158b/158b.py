import pdb

from collections import defaultdict


def get_group(groups, capacity):
    """Return group with size <= capacity and False if no group exists"""

    for i in range(capacity, 0, -1):
        if i in groups and groups[i] > 0:
            return i
    else:
        return False

if __name__ == '__main__':
    n = int(raw_input())

    group_sizes = [int(group_size) for group_size in raw_input().split()]

    groups = defaultdict(int)
    for group_size in group_sizes:
        groups[group_size] += 1

    num_taxis, capacity = 0, 4
    while groups:
        # Look for a group small enough to fit inside the current taxi
        group_size = get_group(groups, capacity)
        if not group_size:
            # No group small enough. So send this taxi on its way and bring in
            # the next one!
            num_taxis += 1
            capacity = 4

            continue

        # Found a group that fits in the current taxi!
        #
        # Put the group in the taxi
        capacity -= group_size
        groups[group_size] -= 1
        if groups[group_size] == 0:
            del groups[group_size] # delete group if there's no one left

    num_taxis += 1 # account for the last unfilled taxi

    print num_taxis
