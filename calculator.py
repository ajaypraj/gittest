def calculation():
    print("Welcome")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    ch=int(input("Enter your choice "))
    print(ch)
    print("Enter the two numbers")
    num1=int(input())
    print("ENter the second number")
    num2=int(input())
    l=list()
    while(1):
        if ch==1:
            ans=num1+num2
            l.append(ans)
            print("Do you want to continue")
            ch1=input("a for continue and b for exit")
            if ch1=='b':
                break
        
            
                
            
    
    for i in l:
        print(i)
    
    
calculation()
