class Student:
    a=10
    def __init__(self):
        Student.a=20
        
    def modify(self):
        Student.a=40
        
    @classmethod
    def modify1(cls):
        cls.a=50
        
    @staticmethod
    def modify2():
        Student.a=1
    
    
    
    
    
s=Student()
s.modify()
print(Student.a)
print(s.a)        
Student.modify1()
print(Student.a)
        
        
        