def insertion(data_list):
    for x in range(1, len(data_list)):
        key = data_list[x]
        y = x-1
        #key를 기준으로 앞에 왼쪽에 위치한 모든 숫자들과 비교 및 위치 이동
        while y>=0 and data_list[y]>key:
            data_list[y+1] = data_list[y] 
            y = y-1

        data_list[y+1] = key

data_list = [20,50,30,10,60,40]
insertion(data_list)
print(data_list)

