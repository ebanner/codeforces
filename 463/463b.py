if __name__ == '__main__':
    n = int(raw_input())
    heights = [int(num) for num in raw_input().split()]

    energy = height = money_spent = 0
    for next_height in heights:
        if next_height > height:
            cost = next_height - height
            if cost > energy:
                money_spent += cost - energy
            else:
                energy -= cost
        else:
            energy += (height - next_height)

        height = next_height

    print money_spent
