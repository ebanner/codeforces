if __name__ == '__main__':
    k = int(raw_input())
    heights = [int(num) for num in raw_input().split()]

    growth = 0
    for i, height in enumerate(sorted(heights, reverse=True)):
        if growth >= k:
            print i
            break

        growth += height

        if growth >= k:
            print i+1
            break
    else:
        print -1
