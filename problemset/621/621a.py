if __name__ == '__main__':
    n = int(raw_input())
    nums = [int(num) for num in raw_input().split()]

    evens = [num for num in nums if num % 2 == 0]
    odds = [num for num in nums if num % 2 == 1]

    odds = sorted(odds, reverse=True)

    total = sum(evens)
    total += sum(odds) if len(odds) % 2 == 0 else sum(odds[:-1])

    print total
