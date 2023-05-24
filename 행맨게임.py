question = list("batman")
answer_list = ["_"] * 6

#단어 맞추기
#char를 입력하고 > question에 동일한 알파벳이 있으면 알파벳으로 바꾸고 출력한다 
#전체 기회는 10번이다. 1)10번 안에 맞추면 you won, 그렇지 못하면 you lose
total_try = 10
while True:
    answer = input("Input the char:")
    idx = 0
    for char in question:
        if answer == char:
            answer_list[idx] = answer
        idx += 1
    print(answer_list)

    if "_" not in answer_list:
        print("You won!")
        break
    if total_try < 1:
        print("You lose")
        break
    total_try -= 1

