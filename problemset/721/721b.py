def maybe_penalty(nb_attempt, k):
    return 5 if nb_attempt % k == 0 else 0

if __name__ == '__main__':
    n, k = [int(num) for num in raw_input().split()]
    P = [raw_input() for _ in range(n)]
    pw = raw_input()

    P = sorted(P, key=len)

    time_elapsed = nb_attempt = 0
    for i, p in enumerate(P):
        if len(p) == len(pw):
            break

        time_elapsed += 1
        nb_attempt += 1
        time_elapsed += maybe_penalty(nb_attempt, k)

    shortest_time = time_elapsed
    shortest_time += 1

    nb_samelen = sum(1 for p in P if len(p) == len(pw))
    longest_time = time_elapsed
    for i in range(nb_samelen):
        if i == nb_samelen-1:
            break

        longest_time += 1
        nb_attempt += 1
        longest_time += maybe_penalty(nb_attempt, k)

    longest_time += 1
    nb_attempt += 1
        
    print shortest_time, longest_time
