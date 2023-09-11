class Person():
    def __init__(self):
        print('person created')

class Student(Person):
    def __init__(self):
        print('student created')

p1=Person()
s1=Student()