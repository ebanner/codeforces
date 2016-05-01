if __name__ == '__main__':
    n = int(raw_input())
    heights = [int(height) for height in raw_input().split()]

    min, max = 100, 0
    for i, height in enumerate(heights):
        if height <= min:
            min, argmin = height, i
        if height > max:
            max, argmax = height, i

    moves = argmax + (n-1-argmin)
    print moves-1 if argmin < argmax else moves
