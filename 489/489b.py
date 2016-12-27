def do_compute(n, m, bskills, gskills):
    nb_pair = i = j = 0
    while True:
        while bskills[i] <= gskills[j]:
            if abs(bskills[i] - gskills[j]) <= 1:
                nb_pair += 1
                j += 1

            i += 1
            if i == n or j == m:
                return nb_pair

        while gskills[j] <= bskills[i]:
            if abs(bskills[i] - gskills[j]) <= 1:
                nb_pair += 1
                i += 1

            j += 1
            if j == m or i == n:
                return nb_pair


if __name__ == '__main__':
    n = int(raw_input())
    bskills = sorted(int(num) for num in raw_input().split())
    m = int(raw_input())
    gskills = sorted(int(num) for num in raw_input().split())

    print do_compute(n, m, bskills, gskills)
