class Test:
    def m1(self,*a):
        total=''
        for x in a:
            total=total+x
            
        print(total)
        
        
t=Test()
t.m1('Durga')
t.m1('Durga','MAi')