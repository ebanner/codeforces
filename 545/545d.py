from itertools import izip

if __name__ == '__main__':
    n = int(raw_input())
    max_waits = sorted(int(num) for num in raw_input().split())

    # Greedy strategy is to sort people by smallest wait times and pick people
    # as long as they are happy. If someone is not happy, then we effectively
    # put them at the end of the line as it makes no sense to include them when
    # there are potentially other people who can still be made happy.
    time_elapsed = nb_in = 0
    for max_wait in max_waits:
        if time_elapsed <= max_wait:
            nb_in += 1
            time_elapsed += max_wait

    print nb_in
