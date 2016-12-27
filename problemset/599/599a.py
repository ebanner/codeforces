if __name__ == '__main__':
    d1, d2, d3 = [int(val) for val in raw_input().split()]

    print min(2*(d1+d2), 2*(d1+d3), 2*(d2+d3), d1+d2+d3)
