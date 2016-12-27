import sys


if __name__ == '__main__':
    M, S = [int(num) for num in raw_input().split()]

    if M == 1 and S == 0:
        print 0, 0
        sys.exit()

    max_num, s = '', S
    for _ in range(M): # build largest string greedily
        if s < 9:
            max_num += str(s)
            s = 0 # zeros from here on out

        else:
            max_num += str(9)
            s -= 9 # append nines as long as possible

    if max_num.startswith('0') or s > 0:
        print -1, -1
        sys.exit()

    min_num = list(reversed(max_num))

    if min_num[0] == '0': # fix leading zero if there is one
        for i in range(M):
            if min_num[i] == '0':
                continue

            min_num[0] = '1'
            min_num[i] = str(int(min_num[i]) - 1)
            break

    print ''.join(min_num), max_num
