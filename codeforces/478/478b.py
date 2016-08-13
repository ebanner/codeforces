def num_pairs(group_size):
    return (group_size*(group_size-1)) / 2


if __name__ == '__main__':
    n, m = [int(num) for num in raw_input().split()]

    max_team_size = n - m + 1
    max_num_friends = num_pairs(max_team_size)

    # Up until doing this problem, I had a single view of n % m, which said,
    # "repeatedly add m until you get to n and the remainder is n % m".
    #
    # This problem demands an additional understanding of m % n, which can be
    # expressed as the following. Take the following example of 8 % 3. For this
    # problem, we are interested in splitting up 8 people into three groups. If
    # we could have partial people, then we would have the following:
    #
    # 8 / 3
    #
    # 2.67 2.67 2.67
    #
    # The amount of decimal defines how much modulus there is. We can rewrite
    # the amount above as:
    #
    # 2.67 2.67 2.67 = 2 + 2 + 2 + (.67 + .67 + .67)
    #                = 2 + 2 + 2 + 2
    #
    # It is not coincidence that the decimal places added up to 2 and that 8 % 3
    # = 2. If n / m exactly, then the decimal places sum is zero and n % m is
    # zero. If n % m is large, then the decimal place will be comparatively
    # large. If n % m is small, then the decimal place will be comparatively
    # small.
    #
    # In general for n / m, we have:
    #
    # n / m
    #
    # floor(n/m) floor(n/m) ... floor(n/m) (m times) + n%m
    #
    # Now to be as balanced as possible, we need to distribute the remainder of
    # n%m over the m floor(n/m) numbers. To do this as evenly as possible, we
    # split it up into ones and distribute them over.
    #
    # min_groups, leftover = [n/m]*m, n%m
    # for i in range(leftover):
    #     min_groups[i] += 1

    # min_num_friends = sum(num_pairs(min_group) for min_group in min_groups)

    min_num_friends = (n%m) * num_pairs(n/m+1) + (m - (n%m))*num_pairs(n/m)

    print min_num_friends, max_num_friends
