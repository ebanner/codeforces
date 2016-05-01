if __name__ == '__main__':
    n = int(raw_input())

    num_passengers = max_capacity = 0
    for _ in range(n):
        a, b = [int(val) for val in raw_input().split()]

        num_passengers -= a
        num_passengers += b

        max_capacity = max(num_passengers, max_capacity)

    print max_capacity
