import sys

if __name__ == '__main__':
    a, b, s = [int(num) for num in raw_input().split()]

    shortest_path = abs(a) + abs(b)

    if s < shortest_path:
        print 'No'
        sys.exit()

    if shortest_path % 2 != s % 2:
        print 'No'
    else:
        print 'Yes'
