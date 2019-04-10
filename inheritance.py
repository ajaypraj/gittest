class P:
    def property(self):
        print("money+gold+power")
    
    def marriage(self):
        print("Subbalaxmi")
        
class C(P):
    def marriage(self):
        super().marriage()
        print("Katrina")
c=C()
c.marriage()
c.property()