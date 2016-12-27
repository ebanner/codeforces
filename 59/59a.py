if __name__ == '__main__':
    word = raw_input()

    num_upper = sum(1 for char in word if char.isupper())

    print word.upper() if num_upper > len(word)/2 else word.lower()
