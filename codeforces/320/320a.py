import sys

if __name__ == '__main__':
    n = raw_input()

    while n:
        if n[:3] == '144':
            n = n[3:]
        elif n[:2] == '14':
            n = n[2:]
        elif n[:1] == '1':
            n = n[1:]
        else:
            print 'NO'
            sys.exit()

    print 'YES'
