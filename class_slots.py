class Person:
    __slots__= ['name','age']

emma = Person()
emma.name = '엠마'
emma.age = 30

emma.email = 'emma@email.com'   #'Person' object has no attribute 'email'