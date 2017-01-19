import sys

if __name__ == '__main__':
    n, a, b = [int(num)-1 for num in raw_input().split()] # zero-based indexing
    A = raw_input()

    if A[a] == A[b]:
        print 0
        sys.exit()

    # Find closest airport which is different
    nb_left = nb_right = 1
    i = a-1
    while True:
        if i == -1:
            break

        if not A[i] == A[a]:
            break
        
        i -= 1
        nb_left += 1

    j = a+1
    while True:
        if j == n:
            break

        if not A[j] == A[a]:
            break
        
        j += 1
        nb_right += 1

    if nb_left == 0:
        min_dist = nb_right
    elif nb_right == 0:
        min_dist = nb_left
    else:
        min_dist = min(nb_left, nb_right)

    print min_dist
