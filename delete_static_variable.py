class Student:
    a=10
    
    def __init__(self):
        Student.a=20
        del Student.a
    @classmethod
    def display_del(cls):
        cls.poo=10
        del cls.poo
s=Student()
Student.display_del()
print(Student.__dict__)
