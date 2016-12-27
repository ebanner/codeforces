def burn(num_burnable, num_burnt, build_cost):
    num_burnt += num_burnable
    num_burnable = 0

    new_burnable = num_burnt / build_cost
    new_burnt = num_burnt % build_cost

    return new_burnable, new_burnt


if __name__ == '__main__':
    a, b = [int(val) for val in raw_input().split()]

    num_hours, num_burnable, num_burnt = 0, a, 0
    while True:
        num_hours += num_burnable
        num_burnable, num_burnt = burn(num_burnable, num_burnt, b)

        if num_burnable == 0:
            break

    print num_hours
