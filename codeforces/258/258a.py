if __name__ == '__main__':
    a = raw_input()

    i = a.find('0')
    print a[:i]+a[i+1:] if not all(bit == '1' for bit in a) else '1'*(len(a)-1)
