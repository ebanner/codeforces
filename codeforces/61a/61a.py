if __name__ == '__main__':
    num1 = [int(char) for char in raw_input()]
    num2 = [int(char) for char in raw_input()]

    print ''.join(str(n1^n2) for n1, n2 in zip(num1, num2))
