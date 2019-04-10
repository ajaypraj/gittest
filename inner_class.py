class Outer:
    def __init__(self):
        print("Outer")
        
    class Inner:
        def __init__(self):
            print("Inner class")
            
        def m1(self):
            print("Inner class method")
            
o=Outer()
i=o.Inner()
i.m1()
Outer().Inner().m1()