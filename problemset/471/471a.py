if __name__ == '__main__':
    sticks = sorted(int(num) for num in raw_input().split())

    if all(stick == sticks[3] for stick in sticks[:4]):
        print 'Bear' if not sticks[4] == sticks[5] else 'Elephant'
    elif all(stick == sticks[3] for stick in sticks[1:5]):
        print 'Bear' if not sticks[0] == sticks[5] else 'Elephant'
    elif all(stick == sticks[3] for stick in sticks[2:]):
        print 'Bear' if not sticks[0] == sticks[1] else 'Elephant'
    else:
        print 'Alien'
