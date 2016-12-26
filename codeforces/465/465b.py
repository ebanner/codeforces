LIST, LETTER = 'list', 'letter'

if __name__ == '__main__':
    n = int(raw_input())
    L = ''.join(num for num in raw_input().split())

    L = [int(num) for num in L.strip('0')]
    state = LIST
    nb_op = 0
    for l in L:
        if state == LIST:
            if l == 0:
                pass # don't need to do anything
            else:
                assert l == 1
                state = LETTER
                nb_op += 1
        else:
            assert state == LETTER
            if l == 0:
                state = LIST
                nb_op += 1
            else:
                assert l == 1
                nb_op += 1

    print nb_op
