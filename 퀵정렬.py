def quick(data_list):
    if len(data_list)<2:
        return data_list
    else:
        key = data_list[0]
        left_data = [data for data in data_list[1:] if data<key]
        right_data = [data for data in data_list[1:] if data>key]
        return quick(left_data)+[key]+quick(right_data)
    
data_list = [20,50,30,10,60,40]
print(quick(data_list))

