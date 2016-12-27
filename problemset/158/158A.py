if __name__ == '__main__':
    n, k = raw_input().split()
    n, k = [int(val) for val in (n, k)]
    scores = raw_input().split()
    scores = [int(score) for score in scores]
    
    threshold = scores[k-1]
    survivors = [score for score in scores if score >= threshold and score > 0]

    print len(survivors)
