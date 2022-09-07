class Dog:
    def walk(self): print("Walks Like a Dog")
    def bark(self): print("barks like a Dog")
    def quack(self): print("Don't Quackk")
    def fur(self): print("Have white and black fur")
class Duck:
    def walk(self): print("Walks Like a Duck")
    def bark(self): print("Don't Bark")
    def quack(self): print("Quackk")
    def fur(self): print("Have Feathers")

def main():
    donald = Duck()
    fido = Dog()
    in_forest(fido)
    in_pond(donald)
def in_forest(a):
    a.bark()
    a.walk()
    print()
def in_pond(b):
    b.quack()
    b.fur()
    print()
if __name__=="__main__":main()
