if __name__ == '__main__':
    n = int(raw_input())
    scores = [int(num) for num in raw_input().split()]

    worst_score = best_score = scores[0]
    num_amazing = 0
    for score in scores[1:]:
        num_amazing += score < worst_score
        num_amazing += score > best_score

        worst_score = min(score, worst_score)
        best_score = max(score, best_score)

    print num_amazing
