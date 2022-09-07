def armstrong(n):
    s = 0
    temp = n
    while n > 0:
        r = n % 10
        s = s + r**3
        n = n // 10
    if s == temp:
        return 1
    else:
        return 0
def pallindrome(n):
    s = 0
    temp = n
    while n > 0:
        r = n % 10
        s = s * 10 + r
        n = n // 10
    if s == temp:
        return 1
    else:
        return 0

print("Check for Armstrong ")
a = int(input("Enter a Number : "))
print(a,"is an Armstrong Number" if armstrong(a) else "Not Armstrong Number")

print("Check for Pallindrome")
b = int(input("Enter a Number : "))
print(b,"is Pallindrome Number" if pallindrome(b) else "Not Pallindrome Number")
