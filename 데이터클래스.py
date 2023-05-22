# class Car:
#     def __init__(self, id, color, brand):
#         self.id = id
#         self.color = color
#         self.brand = brand

# car1 = Car(1, 'WHITE', 'Tesla')
# print(car1)

import inspect
from dataclasses import dataclass, astuple, asdict, replace
from pprint import pprint
from typing import List

@dataclass(frozen=True, order=True) #관련 special method들을 자동으로 생성해줌
# @dataclass
class Car:
    id: int
    color: str = ""
    brand: str = ""

pprint(inspect.getmembers(Car, inspect.isfunction))

car1 = Car(1, 'WHITE','TESLA')
print(car1)

car2 = Car(2, 'BLACK', 'HYUNDAI')
print(f'comparing two objects: {car1 < car2}')

print(astuple(car1))
print(replace(car1, id=3))

