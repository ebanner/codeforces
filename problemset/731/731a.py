import string
from itertools import cycle

if __name__ == '__main__':
    C = raw_input()

    alphabet = string.ascii_lowercase
    F, B = cycle(alphabet), cycle(reversed(alphabet))

    # Set up embossers
    while True:
        backward_letter = next(B)
        if backward_letter == 'a':
            break
    forward_letter = next(F)

    nb_turn = 0
    for c in C:
        nb_forward = nb_backward = 0
        while not forward_letter == c:
            forward_letter = next(F)
            nb_forward += 1

        while not backward_letter == c:
            backward_letter = next(B)
            nb_backward += 1

        nb_turn += min(nb_forward, nb_backward)

    print nb_turn
