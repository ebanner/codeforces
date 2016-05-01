if __name__ == '__main__':
    n = int(raw_input())
    cashes = [int(num) for num in raw_input().split()]

    register = {denom: 0 for denom in (25, 50, 100)}
    for cash in cashes:
        if cash == 25:
            register[25] += 1 # simplest case

        elif cash == 50:
            register[50] += 1
            register[25] -= 1

        elif cash == 100:
            register[100] += 1 # can't use this for anything

            # Greedily try to give out a 50 if we have it
            if register[50] > 0:
                register[50] -= 1
            else:
                register[25] -= 2

            register[25] -= 1

        try: # Verify we stil have positive amount of cash everywhere
            for denom, amount in register.items():
                assert amount >= 0
        except AssertionError:
            print 'NO'

            break
    else:
        print 'YES'
