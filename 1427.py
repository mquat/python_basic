N = input()

mylist = [x for x in N]

mylist.sort(reverse=True)

# result = ''
# for num in mylist:
#     result += num 

#for문 대신, join을 사용해서 결과값을 바로 만들 수도 있다 
result = ''.join(mylist)

print(result)