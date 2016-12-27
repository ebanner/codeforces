if __name__ == '__main__':
    a = int(raw_input())

    nb_step = 0
    while True:
        a += 1
        nb_step += 1

        if '8' in str(a):
            break

    print nb_step
