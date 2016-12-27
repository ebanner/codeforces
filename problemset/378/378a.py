if __name__ == '__main__':
    a, b = [int(num) for num in raw_input().split()]

    nb_a = nb_b = nb_tie = 0
    for i in range(1, 7):
        diff_a, diff_b = abs(i-a), abs(i-b)
        if diff_a == diff_b:
            nb_tie += 1
        elif diff_a < diff_b:
            nb_a += 1
        else:
            nb_b += 1

    print nb_a, nb_tie, nb_b
