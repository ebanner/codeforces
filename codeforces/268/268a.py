from collections import defaultdict


def input_generator(n):
    for _ in range(n):
        yield [int(val) for val in raw_input().split()]


if __name__ == '__main__':
    n = int(raw_input())

    homes, aways_list = zip(*list(input_generator(n)))

    aways = defaultdict(int)
    for away in aways_list:
        aways[away] += 1

    num_collisions = 0
    for home in homes:
        num_collisions += aways[home]

    print num_collisions
