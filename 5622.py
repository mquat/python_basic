#다이얼

answer = input()
dial = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUX","WXYZ"]

# def alphabet(answer):
#     if answer in ["A","B","C"]: return 3
#     elif answer in ["D","E","F"]: return 4
#     elif answer in ["G", "H", "I"] : return 5
#     elif answer in ["J","K","L"] : return 6
#     elif answer in ["M", "N", "O"]: return 7
#     elif answer in ["P","Q","R","S"]: return 8
#     elif answer in ["T","U","V"]: return 9
#     elif answer in ["W", "X", "Y", "Z"]: return 10

# dial_time = 0
# for i in answer:
#     dial_time += alphabet(i)

# print(dial_time)

dial_num = 0
for i in answer:
    for j in range(len(dial)):
        if i in dial[j]:
            dial_num += i+3 

print(dial_num) 