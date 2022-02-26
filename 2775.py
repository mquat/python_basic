#부녀회장이 될테야

#ver1 재귀함수 : 시간 초과 
# floor0 = []
# for i in range(1,15):
#     floor0.append(i)

# def solve(x,y):
#     if x == 0:
#         return y
#     if y == 1:
#         return 1
#     else:
#         return solve(x,y-1)+solve(x-1,y)

# T = int(input())
# for t in range(T):
#     k = int(input())
#     n = int(input())
#     print(solve(k,n))


#ver2 2차 배열 
#floor0 = [1,2,3,....14]
#lst[k][n] = lst[k-1][n]+ lst[k][n-1]