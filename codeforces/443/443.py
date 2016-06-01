import ast

if __name__ == '__main__':
    l = [char.strip() for char in raw_input()[1:-1].split(',')]

    l = [char for char in l if char]

    print len(set(l))
