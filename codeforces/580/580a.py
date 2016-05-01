if __name__ == '__main__':
    n = int(raw_input())
    sequence = [int(val) for val in raw_input().split()]

    subseq_len = max_subseq = 1
    prev_elem = sequence[0]
    for elem in sequence[1:]:
        if elem >= prev_elem:
            subseq_len += 1
            max_subseq = max(max_subseq, subseq_len)
        else:
            subseq_len = 1

        prev_elem = elem

    print max_subseq
