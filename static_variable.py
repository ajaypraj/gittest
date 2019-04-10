class Student:
    cname="DurgsSoft"
    
    def __init__(self):
        Student.cname="BR0"

    def info(self):
        Student.cname="TD"
        
    @classmethod
    def display(cls):
        cls.cname="Pooja"

    @staticmethod
    
    def display1():
        Student.cname="Inside static"
        
Student.f=90
s=Student()
s.info()
s.display()
s.display1()
print(Student.__dict__)
