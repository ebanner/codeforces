if __name__ == '__main__':
    n = int(raw_input())
    heights = [int(num) for num in raw_input().split()]

    max_height, adds = 0, [0]*n
    for i in reversed(range(n)):
        if heights[i] <= max_height:
            adds[i] = max_height - heights[i] + 1

        max_height = max(heights[i], max_height)

    print ' '.join(str(add) for add in adds)
