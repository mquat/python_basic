#구현하지 않은 메소드를 1개 이상 가진다. 자식클래스에서 해당 메소드를 반드시 구현하도록 강제한다. 
#Why we use? - we can define a common API for a set of subclasses

from abc import *

class StudentBase(metaclass = ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def play(self):
        pass


class Student(StudentBase):
    def study(self):
        print('공부하자!')

    def play(self):
        print('놀자!')

james = Student()
james.study()
james.play()


class Student2(StudentBase):
    def study(self):
        print('공부할까?')

    def play(self):
        print('놀까?')

emma = Student2()
emma.study()
emma.play()

