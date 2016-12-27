import string
import re

p1 = re.compile('R(\d+)C(\d+)')
p2 = re.compile('([^\d]+)(\d+)')

idx2alpha = {idx: letter for idx, letter in zip(range(26), string.ascii_uppercase)}
alpha2idx = {letter: idx+1 for idx, letter in idx2alpha.items()}


def num2alpha(num):
    col = []
    while num:
        num -= 1
        mod = num % 26
        col += idx2alpha[mod]
        num /= 26

    return ''.join(reversed(col))

def alpha2num(alpha):
    alpha = list(reversed(alpha))
    return sum(alpha2idx[letter]*26**power for letter, power in zip(alpha, range(len(alpha))))

if __name__ == '__main__':
    n = int(raw_input())

    for _ in range(n):
        cell = raw_input()

        match = p1.match(cell)
        if match:
            row, col = match.group(1), match.group(2)
            new_col = num2alpha(int(col))

            print new_col + row
        else:
            match = p2.match(cell)
            assert match

            col, row = match.group(1), match.group(2)
            new_col = alpha2num(col)

            print 'R{}C{}'.format(row, new_col)
