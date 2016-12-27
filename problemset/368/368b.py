if __name__ == '__main__':
    n, m = [int(num) for num in raw_input().split()]
    A = [int(num) for num in raw_input().split()]

    nb_distincts, distincts = [1]*n, [False]*100001
    distincts[A[-1]] = True # last element has to be distinct
    for i in reversed(range(n-1)):
        a = A[i]

        distinct = distincts[a] == False
        nb_distincts[i] = distinct + nb_distincts[i+1]
        distincts[a] = True

    for _ in range(m):
        q = int(raw_input())
        print nb_distincts[q-1]
