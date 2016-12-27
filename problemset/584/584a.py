def my_range(start, end):
    i = start
    while i < end:
        yield i

        i += 1

if __name__ == '__main__':
    n, t = [int(num) for num in raw_input().split()]

    for num in my_range(10**(n-1), 10**n):
        if num % t == 0:
            print num
            
            break
    else:
        print -1
