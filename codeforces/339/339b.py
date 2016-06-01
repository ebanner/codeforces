if __name__ == '__main__':
    n, m = [int(num) for num in raw_input().split()]
    errands = [int(num)-1 for num in raw_input().split()]

    time = errands[0]
    for start, end in zip(errands, errands[1:]):
        time += (end-start) % n

    print time
