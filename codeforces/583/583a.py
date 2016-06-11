def work_days(n):

    horiz, vert = [0]*n, [0]*n
    for day in range(n**2):
        i, j = [int(num)-1 for num in raw_input().split()]

        if horiz[i] or vert[j]:
            continue # no work today

        horiz[i] = vert[j] = 1

        yield str(day+1)

if __name__ == '__main__':
    n = int(raw_input())

    print ' '.join(list(work_days(n)))
