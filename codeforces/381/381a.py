if __name__ == '__main__':
    n = int(raw_input())
    cards = [int(num) for num in raw_input().split()]

    scores, turn = [0, 0], 0
    while cards:
        scores[turn] += max(cards[0], cards[-1])
        left, right = (1, n) if cards[0] > cards[-1] else (0, -1)
        cards = cards[left:right]
        turn = (turn+1) % 2

    print ' '.join(str(score) for score in scores)
