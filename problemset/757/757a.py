from collections import defaultdict

if __name__ == '__main__':
    C = raw_input()

    L = defaultdict(int)
    for c in C:
        if c not in 'Bulbasr':
            continue

        L[c] += 1

    nb_bulbasaur = 0
    while True:
        # Make a bulbasaur
        L['B'] -= 1
        L['u'] -= 1
        L['l'] -= 1
        L['b'] -= 1
        L['a'] -= 1
        L['s'] -= 1
        L['a'] -= 1
        L['u'] -= 1
        L['r'] -= 1

        if any(count < 0 for count in L.values()):
            break
        else:
            nb_bulbasaur += 1

    print nb_bulbasaur
