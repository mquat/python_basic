#OX퀴즈 

T=int(input())
answer = [input() for i in range(T)]


for i in range(len(answer)):
    score = 0
    total_score = 0 
    for j in range(len(answer[i])):
        if answer[i][j] == "O":
            score += 1 
            total_score += score
        else:
            score = 0

    print(total_score)