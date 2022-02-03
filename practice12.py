#continue, break 

absent = [2,5]
no_book = [7]
for student in range(1,11):
    if student in absent:
        continue    #absent에 해당하는 경우, 다음으로 진행하지 말고 다시 위로 올라가라 
    elif student in no_book:
        print("오늘 수업 여기까지 하겠습니다. {0} 학생은 교무실로 따라와." .format(student))
        break   #바로 반복문 탈출하고 종료 
    print("{0} 학생, 책을 읽어봐" .format(student))