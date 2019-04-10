import sys
n1=18
n=9
while n>0:
    inpn=int(input("Enter the number"))
    if inpn>n1:
        print("Smaller numbers are expected")
    elif inpn<n1:
        print("Bigger number expected")
    elif inpn==n1:
        print("you guessed it correctly.You are winner.")
        sys.exit()
        
    n=n-1
    if n==0:
        print("You have crossed the maximum guessing  limits")
        print("Game end")
        
