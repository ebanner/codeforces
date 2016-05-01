if __name__ == '__main__':
    n = int(raw_input())

    num_drinks = [0]*30

    for i in range(1, len(num_drinks)):
        num_drinks[i] = num_drinks[i-1] + 5*2**(i-1)

    # Keep going until we exceed the number of drinks
    t = 0
    while num_drinks[t] < n:
        t += 1
        
    # Count up the number of people we still have to see
    people_to_go = n - num_drinks[t-1]

    people = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
    i = 0
    while people_to_go:
        if people_to_go-2**(t-1) <= 0:
            print people[i]
            break

        people_to_go -= 2**(t-1)
        i += 1
