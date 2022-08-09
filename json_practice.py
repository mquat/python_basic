#JSON : a syntax for storing and exchanging data
#DO NOT name the file as 'json.py', otherwise 'AttributeError' will be raised

#convert from JSON to Python(dict)
import json
my_profile = '{"name":"Sophie", "age":20, "city":"Seoul"}'  #type: str

x = json.loads(my_profile)

print(x["age"])


#convert from Python(dict) to JSON
my_profile = {
    "name" : "Sophie",
    "age" : 20,
    "city" : "Seoul"
}

y = json.dumps(my_profile)

print(y)
print(type(y))  #type: str, not dict 