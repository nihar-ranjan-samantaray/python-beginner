n = int(input("Enter Any 3 Digit Number : "))
x = n
s = 0
while x != 0:
    r = x % 10
    s = s + r
    x = x // 10
    
print("Sum of The Individual Digit of The Number is",s)
