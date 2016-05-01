if __name__ == '__main__':
    n = int(raw_input())
    values = [int(val) for val in raw_input().split()]

    print -1 if min(values) == 1 else 1
