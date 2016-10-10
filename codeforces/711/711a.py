import sys

if __name__ == '__main__':
    n = int(raw_input())
    
    rows = [raw_input().split('|') for _ in range(n)]

    for i, (left, right) in enumerate(rows):
        if left == 'OO':
            rows[i][0] = '++'
            print 'YES'
            break
        elif right == 'OO':
            rows[i][1] = '++'
            print 'YES'
            break
    else:
        print 'NO'
        sys.exit()

    for row in rows:
        print '|'.join(row)
