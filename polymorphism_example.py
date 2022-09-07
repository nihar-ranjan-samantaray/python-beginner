class Base():
    def __init__(self):
        self.a = 5
        self._b = 2
        self.__c = 2

class Derived(Base):

    def __init__(self):
        Base.__init__(self)
        print(self.a)
        print(self._b)
        print(self.__c)

derivedObj = Derived()

baseObj = Base()
print(baseObj.a)
print(baseObj._b)
print(baseObj.__c)