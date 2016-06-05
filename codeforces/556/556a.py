SMALLEST_IDX = 0 # smallest index for which the number is still there

def move_i(bits, present, i):
    global SMALLEST_IDX
    i_copy = i

    while not present[i]:
        i -= 1

        if i < SMALLEST_IDX:
            SMALLEST_IDX = i_copy
            return -1

    return i

def expand_outward(bits, present, strlen, i, j):

    while 0 <= i and j <= n-1 and bits[i]+bits[j] == 1:
        strlen -= 2
        present[i] = present[j] = False

        i = move_i(bits, present, i)
        j += 1

    return i, j, present, strlen

if __name__ == '__main__':
    n = int(raw_input())
    bits = [int(num) for num in raw_input()]
    present = [True]*n # boolean array for keeping track of whether a number of still there

    i, j, strlen = 0, 1, len(bits)
    while True:
        if j >= n:
            break

        if bits[i] + bits[j] == 1:
            i, j, present, strlen = expand_outward(bits, present, strlen, i, j)

        i, j = j, j+1 # i takes the old place of j - j moves up 1

    print strlen
