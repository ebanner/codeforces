if __name__ == '__main__':
    day, of, time_unit = raw_input().split()
    day = int(day)

    if time_unit == 'week':
        print 53 if 5 <= day <= 6 else 52
    elif time_unit == 'month':
        print 11 if day == 30 else 7 if day == 31 else 12
