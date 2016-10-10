if __name__ == '__main__':
    n = int(raw_input())
    row = raw_input()
    chunks = [len(chunk) for chunk in row.split('W') if chunk]

    print len(chunks)
    if chunks: print ' '.join(str(chunk) for chunk in chunks)
