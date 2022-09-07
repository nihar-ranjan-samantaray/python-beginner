class AnimalActions:
    def bark(self):
        return self._doAction('bark')
    def quack(self):
        return self._doAction('quack')
    def feathers(self):
        return self._doAction('feathers')
    def fur(self):
        return self._doAction('fur')

    def _doAction(self,action):
        if action in self.strings:
            return self.strings[action]
        else:
            return 'The {} has no {}'.format(self.animalName(),action)
    def animalName(self):
        return self.__class__.__name__

class Duck(AnimalActions):
    strings = dict(quack = "Quaaak!",
                   feathers = "The Duck has gray and white faethers")
class Person(AnimalActions):
    strings = dict(bark = "The person says woof",
                   fur = "The Person puts on a fir coat",
                   quack = "The Petson imitiates a duck",
                   feathers = "The Person takes a feather from the ground and shows it")
class Dog(AnimalActions):
    strings = dict(bark = "Arf!",
                   fur = "The Dog has white fur with black spots")

def in_the_forest(duck):
    print(duck.quack())
    print(duck.feathers())
def in_the_doghouse(dog):
    print(dog.bark())
    print(dog.fur())

def main():
    donald = Duck()
    john = Person()
    tommy = Dog()
    print("In The Forest : ")
    for i in(donald,john,tommy):
        in_the_forest(i)
    print("In The Dog House : ")
    for i in (donald,john,tommy):
        in_the_doghouse(i)
if __name__ == "__main__":
    main()
