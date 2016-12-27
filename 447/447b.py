import string

letters = string.ascii_lowercase

if __name__ == '__main__':
    S = raw_input()
    k = int(raw_input())
    W = [int(num) for num in raw_input().split()]

    scores = dict(zip(letters, W))
    argmax = max((w, i) for i, w in enumerate(W))[1]
    max_letter = letters[argmax]
    print sum(i*scores[s] for i, s in enumerate(S+(max_letter*k), start=1))
