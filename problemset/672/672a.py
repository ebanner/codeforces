if __name__ == '__main__':
    n = int(raw_input())

    s = ''.join(str(i) for i in range(1, 1001))
    print s[n-1]
