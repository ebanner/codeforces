def is_capslock(s):
    if s[0].islower():
        return all(char.isupper() for char in s[1:]) # lower then all upper
    else:
        return all(char.isupper() for char in s[1:]) # all upper


if __name__ == '__main__':
    s = raw_input()

    print s.swapcase() if is_capslock(s) else s
