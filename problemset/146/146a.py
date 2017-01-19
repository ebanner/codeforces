import sys

if __name__ == '__main__':
    n = int(raw_input())
    D = raw_input()

    for d in D:
        if d not in '47':
            print 'NO'
            sys.exit()

    if sum(int(d) for d in D[:n/2]) == sum(int(d) for d in D[n/2:]):
        print 'YES'
    else:
        print 'NO'
