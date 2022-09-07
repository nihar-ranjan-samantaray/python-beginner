import sys
print(sys.getrecursionlimit())
def fact(n):
    s = 1
    for i in range(1,n+1):
        s = s*i
        return s
n = int(input("Enter Range : \n"))
res = fact(n)
print("Factorial of",n,"is",res)
