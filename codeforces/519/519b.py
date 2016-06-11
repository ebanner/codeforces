from collections import defaultdict

if __name__ == '__main__':
    n = int(raw_input())

    d = defaultdict(int)
    for error in raw_input().split():
        d[error] += 1

    dd = d.copy()
    for error in raw_input().split():
        dd[error] -= 1

        if dd[error] == 0:
            del dd[error]

    error_1 = dd.keys()[0]

    ddd = d.copy()
    for error in raw_input().split():
        ddd[error] -= 1

        if ddd[error] == 0:
            del ddd[error]

    error_2 = set(ddd.keys()) - set([error_1])

    if not error_2:
        error_2 = error_1
    else:
        error_2 = list(error_2)[0]

    print error_1
    print error_2
