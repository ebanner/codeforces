if __name__ == '__main__':
    num_cups = sum(int(num) for num in raw_input().split())
    num_medals = sum(int(num) for num in raw_input().split())
    n = int(raw_input())

    num_shelves = num_cups / 5
    num_shelves += 1 if num_cups % 5 else 0

    num_shelves += num_medals / 10
    num_shelves += 1 if num_medals % 10 else 0

    print 'YES' if num_shelves <= n else 'NO'
