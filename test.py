class Student:
    cnamae="DurgaSoft"
    
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        
    
s=Student('Durga',10)
print(s.name,s.roll,Student.cnamae)