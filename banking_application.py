import sys
class Bank:
    bName="Cananra"
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
        
    def deposite(self,amount):
        self.balance=self.balance+amount
        print("Your balance is",self.balance)
        
    def withdrawal(self,amount):
        if amount>self.balance:
            print("You have insufficient balance")
            sys.exit()
            
        self.balance=self.balance-amount
        print("Your balance is",self.balance)
        

             
print("Welcome",Bank.bName)
    
name=input("Enter your name")
    
b=Bank(name)
while True:
        ch=input("Enter your choice:For Deposit D \n for Withdrawal W \n and to exit E")
        if ch=='D' or ch=='d':
            amt=float(input("Enter the amount to be deopisted"))
            b.deposite(amt)
            
        elif ch=='w' or ch=='W':
            amt=float(input("enter the amount to be withdrawn"))
            b.withdrawal(amt)
        elif ch=='E' or ch=='e':
            sys.exit()   
        else:
            print("ENter proper choice")
            
            