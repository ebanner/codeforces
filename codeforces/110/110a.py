if __name__ == '__main__':
    num_lucky = 0
    for digit in raw_input():
        if digit in '47':
            num_lucky += 1

    print 'YES' if all(digit in '47' for digit in str(num_lucky)) else 'NO'
