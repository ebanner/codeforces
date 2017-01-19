if __name__ == '__main__':
    n = int(raw_input())
    A = [int(num) for num in raw_input().split()]

    max_increasing = nb_increasing = 1 # count the first element
    for i in range(1, n):
        if A[i-1] >= A[i]:
            nb_increasing = 1
            continue

        nb_increasing += 1
        max_increasing = max(nb_increasing, max_increasing)

    print max_increasing
