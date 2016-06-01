if __name__ == '__main__':
    s = raw_input()

    cond = s.find('0'*7) != -1 or s.find('1'*7) != -1

    print 'YES' if cond else 'NO'
