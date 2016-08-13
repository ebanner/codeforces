if __name__ == '__main__':
    costs = [int(num) for num in raw_input().split()]
    game = [int(num)-1 for num in list(raw_input())]

    cost = 0
    for action in game:
        cost += costs[action]

    print cost
