def decibinary(n):
    if n>1:
        decibinary(n//2)
    print(n%2,end="")

n = int(input())
decibinary(n)
