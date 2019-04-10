def function_name(num,*args,**kwargs):
    for arg in args:
        print(arg)
    print(num)
    
    for k,v in kwargs.items():
        print(k,v)
    
        
har=["Ajahush","saidhia","osjo","Donalodo"]
kw={"Abhay":"Thakur","Kallu":"Kumbhar","Pooja":"Yadav"}
function_name(1000,*har,**kw)