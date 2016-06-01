keyboard = [
    list('qwertyuiop'),
    list('asdfghjkl;'),
    list('zxcvbnm,./'),
]

d = {}
for i in range(len(keyboard)):
    for j in range(len(keyboard[0])):
        d[keyboard[i][j]] = (i, j)


if __name__ == '__main__':
    direction = raw_input()
    chars = raw_input()

    delta = 1 if direction == 'L' else -1

    # http://stackoverflow.com/questions/2436607/how-to-use-re-match-objects-in-a-list-comprehension
    orig_chars = [keyboard[i][j+delta] for char in chars for i, j in [d[char]]] # stylistically dubious!

    print ''.join(orig_chars)
