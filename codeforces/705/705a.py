if __name__ == '__main__':
    n = int(raw_input())

    s = 'I hate'

    for i in range(n-1):
        s = ' '.join([s, 'that I love' if i % 2 == 0 else 'that I hate']) 

    s = ' '.join([s, 'it'])

    print s
