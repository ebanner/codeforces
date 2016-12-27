import string


if __name__ == '__main__':
    s = raw_input()
    t = raw_input()

    letter2loc = dict(zip('abcdefgh', range(1, 9)))

    loc = [letter2loc[s[0]], int(s[1])]
    target = [letter2loc[t[0]], int(t[1])]

    vertical_dict = {True: 'U', False: 'D'}
    horizontal_dict = {True: 'R', False: 'L'}

    move_dict = {'U': 1, 'D': -1, 'L': -1, 'R': 1}

    horiz, vert = target[0]-loc[0], target[1]-loc[1]
    diag_dist = min(abs(horiz), abs(vert))
    print max(abs(horiz)-diag_dist, abs(vert)-diag_dist) + diag_dist
    while (not horiz == 0) and (not vert == 0):
        horiz_move = horizontal_dict[horiz > 0]
        vert_move = vertical_dict[vert > 0]

        print horiz_move + vert_move

        loc[0] += move_dict[horiz_move]
        loc[1] += move_dict[vert_move]

        horiz, vert = target[0]-loc[0], target[1]-loc[1]

    if not vert == 0:
        while abs(vert) > 0:
            vert_move = vertical_dict[vert > 0]
            print vert_move
            loc[1] += move_dict[vert_move]
            vert = target[1]-loc[1]
    elif not horiz == 0:
        while abs(horiz) > 0:
            horiz_move = horizontal_dict[horiz > 0]
            print horiz_move
            loc[0] += move_dict[horiz_move]
            horiz = target[0]-loc[0]
