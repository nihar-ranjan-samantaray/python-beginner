class computer():
    def __init__(self):
        self.name = "Nihar"
        self.age = 23
    #def update(self):
    #   self.name = "x"
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False
c1 = computer()
c2 = computer()

#c1.name = "Rashi"
if c1.compare(c2):
    print("They Are Same")
print(c1.name)
print(c2.name)
