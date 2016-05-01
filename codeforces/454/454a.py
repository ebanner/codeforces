from collections import deque


if __name__ == '__main__':
    n = int(raw_input())

    stack = deque([(1, 'expand')])

    while stack:
        level, action = stack.popleft()

        if action == 'expand':
            print '{}{}{}'.format('*'*((n-level)/2), 'D'*level, '*'*((n-level)/2))

            if level == n: # base case - don't add anything to the stack
                pass
            else: # recursive case
                stack.appendleft([level, 'finish'])
                stack.appendleft([level+2, 'expand'])

        elif action == 'finish':
            print '{}{}{}'.format('*'*((n-level)/2), 'D'*level, '*'*((n-level)/2))
