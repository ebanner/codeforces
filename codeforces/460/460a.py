def do_day(num_pairs, day, mom_every):
    num_pairs -= 1 # vasya wears a pair of socks

    if day % mom_every == 0:
        num_pairs += 1

    return num_pairs

if __name__ == '__main__':
    n, m = [int(val) for val in raw_input().split()]

    num_pairs, mom_every, day = n, m, 1
    while num_pairs:
        num_pairs = do_day(num_pairs, day, mom_every)

        day += 1

    print day - 1
