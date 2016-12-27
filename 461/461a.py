if __name__ == '__main__':
    n = int(raw_input())
    ints = sorted(int(num) for num in raw_input().split())

    coeffs = range(1, n+1)
    coeffs[-1] = n-1 # biggest two numbers counted same number of times
    coeffs = [coeff+1 for coeff in coeffs] # each number is counted an extra time

    print sum(coeff*int for coeff, int in zip(coeffs, ints))
