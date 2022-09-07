a = int(input())
b = int(input())

if a>b:
    num1 = a
    num2 = b
else:
    num1 = b
    num2 = a
while num1%num2 != 0:
    rem = num%num2
    num1 = num2
    num2 = rem
print("GCD is {}".format(num2))
