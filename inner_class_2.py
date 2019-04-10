class Person:
    def __init__(self,name,dd,month,year):
        self.name=name
        self.dob=self.DOB(dd,month,year)
        
    def display(self):
        print(self.name)
        self.dob.display()
        
    class DOB:
        def __init__(self,dd,month,year):
            self.dd=dd
            self.month=month
            self.year=year
        def display(self):
            print(self.dd)
            print(self.month)
            print(self.year)
            
p=Person('Ajay',26,8,1991)
p.display()