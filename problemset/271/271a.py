if __name__ == '__main__':
    year = int(raw_input())

    year += 1
    while True:
        if len(set(str(year))) == 4:
            print year
            break

        year += 1
