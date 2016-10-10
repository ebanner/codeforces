if __name__ == '__main__':
    n = int(raw_input())
    workouts = [int(num) for num in raw_input().split()]

    d = {}
    d['chest'] = sum(workouts[::3])
    d['biceps'] = sum(workouts[1::3])
    d['back'] = sum(workouts[2::3])

    print sorted(d, key=d.get, reverse=True)[0]
