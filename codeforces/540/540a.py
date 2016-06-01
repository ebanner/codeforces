if __name__ == '__main__':
    n = int(raw_input())
    num1 = [int(num) for num in raw_input()]
    num2 = [int(num) for num in raw_input()]

    num_moves = 0
    for start, end in zip(num1, num2):
        num_moves += min(abs(end-start), start+10-end, 10-start+end)

    print num_moves
