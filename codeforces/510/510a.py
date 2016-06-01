if __name__ == '__main__':
    n, m = [int(num) for num in raw_input().split()]

    right = ['.']*m
    right[-1] = '#'
    right = ''.join(right)

    left = ['.']*m
    left[0] = '#'
    left = ''.join(left)

    middle = '#'*m

    snake = ['']*n
    for i in range(0, n, 2):
        snake[i] = middle

    for i in range(1, n, 4):
        snake[i] = right

    for i in range(3, n, 4):
        snake[i] = left

    print '\n'.join(snake)
