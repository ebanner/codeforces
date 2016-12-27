if __name__ == '__main__':
    s = raw_input()

    char = (char for char in 'hello')
    h_char = next(char)

    for s_char in s:
        if s_char != h_char:
            continue

        # Character matches! Try to get the next character in 'hello'
        try:
            h_char = next(char)
        except StopIteration:
            print 'YES' # no more characters to get!
            break
    else:
        print 'NO'
