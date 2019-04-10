from Crypto.SelfTest import SelfTestError
class Employee:
    def __init__(self,empn,empname,empsal):
        self.empn=empn
        self.empname=empname
        self.empsal=empsal
        
        
    def display(self):
        print("EMP NO",self.empn)
        print("EMP Name",self.empname)
        print("EMP sal",Self.empsal)
        
        
class Test:
    def modify(emp):
        emp.empn=emp.empn+10
        emp.display()
        

e=Employee(10,'Aminata',1100)
#Test.m1(e)
#print(e.empsal)
Test.modify(e)