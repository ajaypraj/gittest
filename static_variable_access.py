class Student:
    a=10
    
    
    def __init__(self):
        print("Inside Constructor")
        print(self.a)
        print(Student.a)
        
    def display(self):
        print(self.a)
        print(Student.a)
        
    @classmethod
    
    def display1(cls):
        print("Inside a class method")
        print(cls.a)
        print(Student.a)
        
        
    @staticmethod
    def print_a():
        print(Student.a)
        
        
        
        
        
        
        
        
        
s=Student()
s.display()
s.display1()
Student.print_a()
