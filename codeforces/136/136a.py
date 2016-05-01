if __name__ == '__main__':
    n = int(raw_input())

    forwards, backwards = [0]*n, [0]*n

    forwards = [int(p)-1 for p in raw_input().split()]

    for i, forward in enumerate(forwards):
        backwards[forward] = i

    print ' '.join(str(backward+1) for backward in backwards)
