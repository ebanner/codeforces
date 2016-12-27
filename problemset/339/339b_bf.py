if __name__ == '__main__':
    n, m = [int(num) for num in raw_input().split()]
    errands = [int(num)-1 for num in raw_input().split()]

    house = time = 0
    for errand in errands:
        while not house == errand:
            house = (house+1) % n
            time += 1

    print time
