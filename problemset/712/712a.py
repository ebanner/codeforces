if __name__ == '__main__':
    n = int(raw_input())
    A = [int(num) for num in raw_input().split()]

    B = [0]*n
    B[-1] = A[-1]
    B[-2] = A[-2] + B[-1]

    bodd, beven = B[-1], 0
    for i in range(3, n+1):
        B[-i] = A[-i]

        if i % 2 == 0:
            bodd += B[-i+1]
            B[-i] += bodd - beven
        else:
            beven += B[-i+1]
            B[-i] += beven - bodd

    print ' '.join(str(b) for b in B)
