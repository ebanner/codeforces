def stmt_generator():
    while True:
        yield raw_input()

if __name__ == '__main__':

    n = int(raw_input())

    statement = stmt_generator()

    X = 0
    for _ in range(n):
        stmt = next(statement)

        X = X+1 if stmt.find('++') != -1 else X-1

    print X
