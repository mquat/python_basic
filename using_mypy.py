#https://mypy.readthedocs.io/en/stable/
#mypy [file_name.py]
#This makes mypy type check your file and print out any errors it finds. 

def greeting(name: str) -> int:
    return "Hello " + name

print(greeting('emma'))     #Incompatible return value type (got "str", expected "int")

