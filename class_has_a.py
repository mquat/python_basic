#has-a relationship: PersonList class has a Person class

class Person:
    def greeting(self):
        return '안녕하세요'

class PersonList:
    def __init__(self):
        self.person_list = []

    def add_person(self, person):
        self.person_list.append(person)
        return self.person_list

emma = Person()

print(emma)
print(PersonList().add_person(emma))      

