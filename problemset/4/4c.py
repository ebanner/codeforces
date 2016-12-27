if __name__ == '__main__':
    n = int(raw_input())

    d = {}
    for _ in range(n):
        user = raw_input()

        if user in d:
            print user + str(d[user])
            d[user] += 1
        else:
            d[user] = 1
            print 'OK'
