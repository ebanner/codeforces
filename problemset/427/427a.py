if __name__ == '__main__':
    n = int(raw_input())
    events = [int(num) for num in raw_input().split()]

    nb_recruits = nb_untreated = 0
    for event in events:
        if event == -1:
            if nb_recruits == 0:
                nb_untreated += 1
            else:
                nb_recruits -= 1
        else:
            nb_recruits += event

    print nb_untreated
