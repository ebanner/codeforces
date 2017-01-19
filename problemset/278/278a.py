if __name__ == '__main__':
    n = int(raw_input())
    D = [int(num) for num in raw_input().split()]
    s, t = [int(num)-1 for num in raw_input().split()] # zero-based indexing

    i = j = s
    di = 0
    while i != t:
        di += D[i]
        i = (i+1) % n

    dj = 0
    while j != t:
        j = (j-1) % n
        dj += D[j]

    print min(di, dj)
