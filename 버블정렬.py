def bubble(data_list):
    for x in range(0, len(data_list)-1):
        for y in range(0, len(data_list)-1-x):
            #둘을 비교하여 더 큰 숫자를 뒤로 보낸다(자리를 교환한다)
            if data_list[y]>data_list[y+1]:
                data_list[y], data_list[y+1] = data_list[y+1], data_list[y]

data_list = [20,50,30,10,60,40]
bubble(data_list)
print(data_list)

