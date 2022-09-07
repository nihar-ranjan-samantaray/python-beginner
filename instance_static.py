class student:
    x = "NRS"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod
    def info(cls):
        return cls.x
    @staticmethod
    def getschool():
        print("Hey There")
s1 = student(34,56,43)
obj2 = student(34,56,75)
print(s1.m1,s1.m2,s1.m3,student.x)
print(s1.avg())
print(student.info())
student.getschool()

