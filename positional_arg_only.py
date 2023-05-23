def add_one(a: int, /):
    return a+1

print(add_one(num=1))   #positional-only argument error
print(add_one(1))

