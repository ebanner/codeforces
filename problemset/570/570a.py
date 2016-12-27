def argmax(iterable):
    return max(enumerate(iterable), key=lambda x: x[1])[0]

if __name__ == '__main__':
    n, m = [int(num) for num in raw_input().split()]
    votes = [[int(num) for num in raw_input().split()] for _ in range(m)]

    cities_won = [0]*n
    for city in votes:
        cities_won[argmax(city)] += 1

    print argmax(cities_won) + 1
