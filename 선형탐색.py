def linear_search(data_list, key):
    for x in range(0, len(data_list)):
        if data_list[x] == key:
            return x

data_list = [20,50,30,10,60,40]
print(linear_search(data_list, 10))

