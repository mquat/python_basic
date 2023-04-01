#a nested function: when we call the anonymous function, we are able to access to the 'name' variable of the outer function
#3 characteristics of Closure: 1) a nested function, 2) has access to a free variable in outer scope, 3) returned from the enclosing function
#Free variable: a variable which is not bound in the local scope

## example 1
def greet():
    name = "John"   #free variable

    #a nested anonymous function
    return lambda : "Hi, welcome " + name

message = greet()   #Generally, when we call greet() then the 'name' variable will be destroyed as the execution of the outer function is completed
print(message())


## example 2
def multiply():
    a = 10
    b = 2       

    def mul_add(x):
        return (a * x) + b
    return mul_add

mul = multiply()
print(mul(2))   #return 22



## example 3
def calculate():
    num = 1
    
    def odd_num():
        nonlocal num    #nonlocal is a must to work with immutable variables such as string or integer
        num += 2 
        return num
    return odd_num

odd1 = calculate()

print(odd1())
print(odd1())
print(odd1())    #return 7

odd2 = calculate()

print(odd2())   #return 3


## example 4
def multiplier(n):
    def inner_function(m):
        return n * m
    return inner_function

time3 = multiplier(3)

print(time3(9))    #return 27
print(time3(10))    #return 30


## Conclusion: When to use closures? - 1) use free variables, 2) prevent direct access to data(variables used for the inner function can be hided)

