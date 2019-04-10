class Book:
    def __init__(self,pages):
        self.pages=pages
    
    def __str__(self):
        return str(self.pages)
    def __add__(self,other):
        total=self.pages+other.pages
        b=Book(total)
        return b


b1=Book(100)
b2=Book(200)
b3=Book(200)
print(b1+b2)

print(b2+b3)
print(b1+b2+b3)