from collections import defaultdict

if __name__ == '__main__':
    name1 = raw_input()
    name2 = raw_input()
    jumbled = raw_input()

    d = defaultdict(int)
    for char in jumbled:
        d[char] += 1

    for char in name1 + name2:
        d[char] -= 1

    for char, count in d.items():
        if not count == 0:
            print 'NO'

            break
    else:
        print 'YES'
