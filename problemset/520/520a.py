if __name__ == '__main__':
    n = int(raw_input())
    s = [char.lower() for char in raw_input()]

    print 'YES' if len(set(s)) == 26 else 'NO'
