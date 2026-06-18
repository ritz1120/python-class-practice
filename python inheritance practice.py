class student:
    def __init__(self,n,c):
        self.n=n
        self.c=c
o=student("rithika","ece")
print(o.n)

#single inheritance
class mom:
    def eyes(self):
        print("eyes...")
class child(mom):
    def nose(self):
        print("nose...")
o=child()
o.eyes()

#multiple inheritance
class mom:
    def eyes(self):
        print("eyes...")
class dad:
    def ears(self):
        print("nose...")

class child(mom,dad):
    def nose(self):
        print("nose...")
o=child()
o.ears()

#multilevel inheritance
class grandmother:
    def eyes(self):
        print("eyes...")
class mother(grandmother):
    def ears(self):
        print("ears...")
class daughter(mother):
    def nose(self):
        print("nose...")
o=child()
o.eyes()

#hierarchial inheritance
class mother:
    def eyes(self):
        print("eyes")
class daughter(mother):
    def nose(self):
        print("nose")
class son(mother):
    def mouth(self):
        print("Mouth")
o=son()
o.eyes()

#hybrid inheritance
class grandmother:
    def eyes(self):
        print("eyes...")
class mother(grandmother):
    def ears(self):
        print("ears...")
class aunt(grandmother):
    def nose(self):
        print("nose...")
class daughter(mom,aunt):
    def haircolour(self):
        print("haircolour")
o=daughter()
o.nose()


        
        


