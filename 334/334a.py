if __name__ == '__main__':
    n = int(raw_input())

    bags = [str(i) for i in range(1, n**2+1)]

    for i in range(n):
        left, right = i*(n/2), (i+1)*(n/2)

        if i == 0:
            print ' '.join(bags[left:right]) + ' ' + ' '.join(bags[-right:])
        else:
            print ' '.join(bags[left:right]) + ' ' + ' '.join(bags[-right:-left])
