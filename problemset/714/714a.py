if __name__ == '__main__':
    l1, r1, l2, r2, k = [int(num) for num in raw_input().split()]

    if l1 <= l2 and l2 <= r1 and r1 <= r2:
        time = r1 - l2 + 1 # Sonya arrives first and there is some overlap with Filya
        time -= l2 <= k <= r1
    elif l1 <= l2 and l2 <= r2 and r2 <= r1:
        time = r2 - l2 + 1 # Filya subset of Sonya
        time -= l2 <= k <= r2
    elif l1 <= r1 and r1 < l2 and l2 <= r2:
        time = 0 # Sonya arrives and leaves before Filya arrives
    elif l2 <= l1 and l1 <= r2 and r2 <= r1:
        time = r2 - l1 + 1 # Filya arrives first and there is some overlap with Sonya
        time -= l1 <= k <= r2
    elif l2 <= l1 and l1 <= r1 and r1 <= r2:
        time = r1 - l1 + 1 # Sonya subset of Filya
        time -= l1 <= k <= r1
    elif l2 <= r2 and r2 < l1 and l1 <= r1:
        time = 0 # Filya arrives and leaves before Sonya

    print time
