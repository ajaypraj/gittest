class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def __mul__(self,other):
        return self.salary * other.time
        
class Timesheet:
    def __init__(self,name,time):
        self.name=name
        self.time=time
        
e=Employee("Durga",1000)
t=Timesheet("Durga",20)

print(e*t)