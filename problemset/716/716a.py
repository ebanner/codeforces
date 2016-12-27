from itertools import izip

if __name__ == '__main__':
    n, c = [int(num) for num in raw_input().split()]
    times = [int(num) for num in raw_input().split()]

    delays = [d2-d1 for d1, d2 in izip(times, times[1:])]

    nb_word = 0
    for delay in delays:
        nb_word += 1 # write a word

        # process delay
        if delay > c:
            nb_word = 0 # clear words

    nb_word += 1 # always write one word last word
    print nb_word
