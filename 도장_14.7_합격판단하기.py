kor, eng, math, sci = map(int, input().split())

if 0<=kor<=100 and 0<=eng<=100 and 0<=math<=100 and 0<=sci<=100:
    if (kor+eng+math+sci)/4 >=80:
        print('합격')
    else:
        print('불합격')
else:
    print('잘못된 점수')