class arith:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2

        s3 = arith(m1,m2)
        return s3
    def __gt__(self,other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

m111 = int(input())
m11 = int(input())
m222 = int(input())
m22 = int(input())
s1 = arith(m111,m11)
s2 = arith(m222,m22)

s3 = s1 + s2
if s1 > s2:
    print("Win S1")
else:
    print("Win S2")
