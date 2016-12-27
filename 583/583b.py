class Bumper:
    def __init__(self, iterable):
        self.iterable = iterable
        self.n = len(iterable)
        self.i = 0
        self.direction = 'right'
        self.nb_turn = 0

    def __iter__(self):
        return self

    def next(self):
        i = self.i

        if self.i == self.n-1:
            self.i -= 1
            self.direction = 'left'
        elif self.i == 0:
            self.i += 1
            self.direction = 'right'
        else:
            self.i = self.i+1 if self.direction == 'right' else self.i-1

        return i

if __name__ == '__main__':
    n = int(raw_input())
    nums = [int(num) for num in raw_input().split()]

    num, cracked, nb_info, nb_turn, first = iter(Bumper(nums)), [False]*n, 0, 0, True
    while True:
        i = next(num)
        if not first and (i == 0 or i == n-1):
            nb_turn += 1

        first = False

        if cracked[i]:
            continue # don't do anything if the computer is already cracked

        if nb_info < nums[i]:
            continue # can't crack the computer with current level of info

        # computer is not cracked and we are able to crack it
        cracked[i], nb_info = True, nb_info+1

        if nb_info == n:
            break # cracked every computer

    if n == 1:
        print 0
    else:
        print nb_turn if not (i == 0 or i == n-1) else nb_turn-1
