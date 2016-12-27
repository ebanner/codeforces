if __name__ == '__main__':
    n, d = [int(num) for num in raw_input().split()]

    nb_beat = max_beat = 0
    for _ in range(d):
        if not all(int(bit) for bit in raw_input()):
            nb_beat += 1
        else:
            max_beat = max(max_beat, nb_beat)
            nb_beat = 0

    print max(max_beat, nb_beat)
