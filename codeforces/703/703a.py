if __name__ == '__main__':
    n = int(raw_input())

    nb_m = nb_c = 0
    for _ in range(n):
        m, c = [int(num) for num in raw_input().split()]
        if m > c:
            nb_m += 1
        elif c > m:
            nb_c += 1

    print 'Mishka' if nb_m > nb_c else 'Chris' if nb_c > nb_m else 'Friendship is magic!^^'
