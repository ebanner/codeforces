if __name__ == '__main__':
    n = raw_input()

    last_removed = n[:-1]
    penultimate_removed = n[:-2] +n[-1]

    print max(int(n), int(last_removed), int(penultimate_removed))
