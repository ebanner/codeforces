if __name__ == '__main__':
    s1 = raw_input()
    s2 = raw_input()

    for c1, c2 in zip(s1, s2):
        if c1.lower() == c2.lower():
            continue
        else:
            print -1 if c1.lower() < c2.lower() else 1

            break
    else:
        print 0
