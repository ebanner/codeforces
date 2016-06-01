if __name__ == '__main__':
    n = int(raw_input())

    magnets = [raw_input() for _ in range(n)]

    num_groups = 0
    group_id = magnets[0]
    for magnet in magnets[1:]:
        if magnet == group_id:
            continue

        num_groups += 1
        group_id = magnet

    num_groups += 1

    print num_groups
