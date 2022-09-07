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
    for o in(donald,fido):
        o.walk()
        o.bark()
        o.quack()
        o.fur()
        print()
if __name__=="__main__":main()
