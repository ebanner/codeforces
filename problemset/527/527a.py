def gcd(a, b, n):
    if b == 0:
        return n

    return gcd(b, a%b, n+a/b)

if __name__ == '__main__':
    a, b = [int(num) for num in raw_input().split()]

    print gcd(a, b, 0)
