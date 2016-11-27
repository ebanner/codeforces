import sys

def choose(n, k):
    return fact(n) / (fact(n-k) * fact(k))

def fact(n):
    return 1 if n == 0 else n * fact(n-1)

if __name__ == '__main__':
    S1 = list(raw_input())
    S2 = list(raw_input())

    s1_plus = sum(1 for s1 in S1 if s1 == '+')
    s1_minus = sum(1 for s1 in S1 if s1 == '-')

    s2_plus = sum(1 for s2 in S2 if s2 == '+')
    s2_minus = sum(1 for s2 in S2 if s2 == '-')

    if not '?' in S2:
        print 1. if s1_plus == s2_plus and s1_minus == s2_minus else 0.
        sys.exit()

    nb_plus_needed = abs(s1_plus - s2_plus)
    nb_question = sum(1 for s2 in S2 if s2 == '?')

    if nb_question < nb_plus_needed or s2_plus > s1_plus:
        print 0.
        sys.exit()
    else:
        print choose(n=nb_question, k=nb_plus_needed) * 0.5**nb_question
