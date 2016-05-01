def example_generator():
    while True:
        p, v, t = raw_input().split()
        p, v, t = [int(vote) for vote in (p, v, t)]

        yield p, v, t

def will_solve(p, v, t):
    return 1 if p+v+t >= 2 else 0

if __name__ == '__main__':
    n = int(raw_input())

    example = example_generator()

    num_will_solve = 0
    for _ in range(n):
        p, v, t = next(example)

        num_will_solve += will_solve(p, v, t)

    print num_will_solve
