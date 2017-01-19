if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    c = int(raw_input())

    nb_fruit = 0
    while True:
        if a < 1 or b < 2 or c < 4:
            break

        a -= 1
        b -= 2
        c -= 4

        nb_fruit += 7

    print nb_fruit
