from typing import Dict


def isArmstrong(n):
    res = 0
    temp = n
    while n > 0:
        r = n % 10
        res = res + r ** 3
        n = n // 10
    if res == temp: return 1
    else: return 0

def isPallindrome(n):
    res = 0
    temp = n
    while n > 0:
        r = n % 10
        res = res * 10 + r
        n = n // 10
    if res == temp: return 1
    else: return 0

def recursion(n):
    if n == 1:
        return n
    else:
        return n * recursion(n-1)

# a = int(input())
# print(a," is Armstong Number" if isArmstrong(a) else " is not Armstrong Number")
# b = int(input())
# print(b," is Pallindrome Number" if isPallindrome(b) else " is not Pallindrome Number")

# print(recursion(5))

# List = list()
# List.append(1)
# print(List)
# List.append("Helllo")
# print(List)
# dict1 = dict(value=4)
# List.append(dict1)
# print(List)
# List2 = [1,2,3,4,5]
# set1 = set(List2)
# print(set1)
# List.append(set1)
# print(List)
# set2 = set(["Nihar", "Ranjan", "Samantaray"])
# print(set2)
# set3 = set("Nihar")
# print(set3)
# tuple1 = tuple(List)
# print(tuple1)

class Animal():
    a = 20
    def speak(self):
        print("Can speak")
    def run(self):
        print("Animal can run")
class Dog(Animal):
    
    def bark(self):
        print("Can bark")
    def run(self):
        b = super().a
        print(b)
        print("Dog can run")
    

obj = Dog()
obj.bark()
obj.speak()
obj.run()


def add(x,y,z=0):
    return x + y + z

print(add(2,4))
print(add(5,3,7))


class Car():
    def tyre(self):
        print("Have 4 tyres")
    def handle(self):
        print("Have round handle")
class Bike():
    def tyre(self):
        print("Have 2 tyres")
    def handle(self):
        print("Have straight handle")

def func(obj):
    obj.tyre()
    obj.handle()

obj_car = Car()
obj_bike = Bike()
func(obj_car)
func(obj_bike)

element = ['apple','banana','cherry','kiwi']
newList = [x for x in element if 'a' in x]
print(newList)
a = [1,2,3,4,5,6,7,8,9,10]
res = [x for x in a if x % 2 != 0 ]
print(res)

newFunction = lambda x,y : x ** y
print(newFunction(5,2))

def myFunc(n):
    return lambda a :  a * n
myDoubler = myFunc(2)
print(myDoubler(11))

def addition(a,b):
    return a + b
ress = map(addition, (2, 3))
print(ress)