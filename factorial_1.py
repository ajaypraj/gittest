def fact(n):
    if n>1:
        return n*fact(n-1)
    else:
        return 1
    
    
p=fact(5)

print(p)