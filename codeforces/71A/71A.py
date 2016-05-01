def example_generator():
    while True:
        yield raw_input()

def do_abbreviation(long_word):
    if len(long_word) > 10:
        long_word = long_word[0] + str(len(long_word)-2) + long_word[-1]

    print long_word

if __name__ == '__main__':
    n = int(raw_input())

    example = example_generator()

    for _ in range(n):
        long_word = next(example)

        do_abbreviation(long_word)
