import sys

if __name__ == '__main__':
    n = int(raw_input())
    A = ''.join(raw_input().split())

    if all(a == '0' for a in A):
        print 0
        sys.exit()

    nb_splits = [len(zeros)+1 for zeros in A.strip('0').split('1')]
    nb_path = 1
    for nb_local_split in nb_splits:
        nb_path *= nb_local_split

    print nb_path
