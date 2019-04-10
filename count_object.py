class Test:
    count=0
    def __init__(self):
        Test.count=Test.count+1
     
     
    @classmethod   
    def getNo(cls):
        print("The no of object created",cls.count)
        

t1=Test()
t2=Test()
print(Test.getNo())
        
