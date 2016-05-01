if __name__ == '__main__':
    n = int(raw_input())

    props = [int(val) for val in raw_input().split()]

    print sum(props) / float(n)
