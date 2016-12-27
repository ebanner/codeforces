if __name__ == '__main__':
    n = int(raw_input())

    main_numer = n * (n+1)
    resid_numer = n * (n-1) * (n-2)

    print main_numer/2 + resid_numer/6
