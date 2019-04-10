#x=10
class Test:
    def m1(self):
        global x
        x=10
        print(x)
        
    def m2(self):
        print(x)
        
t=Test()
t.m1()
t.m2()