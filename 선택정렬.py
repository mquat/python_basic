def selection(data_list):
    for x in range(0, len(data_list)-1):
        min_x = x
        #현재 range 내에서 최소값 찾기
        for y in range(x+1, len(data_list)):
            if data_list[y] < data_list[min_x]:
                min_x = y
        #최소값 찿은 후, exchange
        data_list[x], data_list[min_x] = data_list[min_x], data_list[x]


data_list = [20,50,30,10,60,40]
selection(data_list)
print(data_list)

