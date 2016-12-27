if __name__ == '__main__':
    k, r = [int(num) for num in raw_input().split()]

    price = 0
    while True:
        price += k
        
        if price % 10 == 0 or price % 10 == r:
            break

    print price / k
