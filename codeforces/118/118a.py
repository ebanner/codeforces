def xform_generator(string):
    for c in string:
        if c.lower() in 'aoyeui':
            continue

        yield '.'

        if c.isupper():
            c = c.lower()

        yield c

if __name__ == '__main__':
    string = raw_input()

    xformed_str = list(xform_generator(string))

    print ''.join(xformed_str)
