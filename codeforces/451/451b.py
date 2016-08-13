if __name__ == '__main__':
    n = int(raw_input())
    a = [int(num) for num in raw_input().split()]

    j = k = 0 # set these guys just in case `a` is completely sorted
    for i in range(n-1):
        if a[i] <= a[i+1]:
            continue # nothing to see here

        # start of non-increasing sequence! ride it out...
        j = k = i
        while k < n-1 and a[k] >= a[k+1]:
            k += 1

        a[j:k+1] = a[k:j-1:-1] if not j == 0 else a[k::-1] # reverse the slice

        break # we only get to reverse a single slice

    # verify the list is sorted
    for aa, aaa in zip(a, a[1:]):
        if aa > aaa:
            print 'no'
            break
    else:
        print 'yes'
        print j+1, k+1
