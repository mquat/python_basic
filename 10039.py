def score_average():
    scores = []
    for _ in range(5):
        x = int(input())
        if x < 40:
            scores.append(40)
        else:
            scores.append(x) 

    print(sum(scores)//5)

score_average()