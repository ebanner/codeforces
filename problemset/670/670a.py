if __name__ == '__main__':
    n = int(raw_input())

    # min case - start with 5 work days
    days_left, min_vaca = n, 0
    while True:
        days_left -= 5
        if days_left <= 0:
            break
        
        min_vaca += min(days_left, 2)
        days_left -= 2

    # max case - start with 2 vacation days
    days_left, max_vaca = n, 0
    while True:
        max_vaca += min(days_left, 2)
        days_left -= 2

        days_left -= 5
        if days_left <= 0:
            break

    print min_vaca, max_vaca
