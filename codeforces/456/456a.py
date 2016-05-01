def input_generator(n):
    for _ in range(n):
        p, q = [int(num) for num in raw_input().split()]

        yield p, q

if __name__ == '__main__':
    n = int(raw_input())

    laptops_info = sorted(list(input_generator(n)))

    for (p1, q1), (p2, q2) in zip(laptops_info, laptops_info[1:]):
        if p2 > p1 and q2 < q1:
            print 'Happy Alex'

            break
    else:
        print 'Poor Alex'
