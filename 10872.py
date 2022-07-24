N = int(input())

##첫번째 방식 
# x = 1
# for i in range(N,0,-1):
#     x *= i 

# print(x)


##재귀함수 방식
##2! = 2 * 1
##3! = 3 * 2!
##4! = 4 * 3! 
def factorial(n):
    #n이 0이나 1이면, return 1
    if n <= 1:
        return 1
    #그렇지않으면 재귀함수
    result = n * factorial(n-1)
    return result

print(factorial(N))