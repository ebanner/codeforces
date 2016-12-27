def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a

    if a > b:
        return gcd(b, a%b)
    else:
        return gcd(a, b%a)

if __name__ == '__main__':
    a, b, n = [int(val) for val in raw_input().split()]

    num_stones, turn, values = n, 0, [a, b]
    while num_stones:
        num_stones -= gcd(values[turn], num_stones)
        turn = (turn+1) % 2

    print (turn+1) % 2
