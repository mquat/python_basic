#나머지
lst = []
for i in range(10):
    lst.append(int(input()))
    lst[i] % 42 

new_lst = set(lst)
print(len(new_lst))

