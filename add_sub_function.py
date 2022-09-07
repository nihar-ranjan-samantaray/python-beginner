a = int(input("Enter A Number : "))
b = int(input("Enter Another Number : "))

def add_sub(x,y):
    c = x + y
    d = x - y
    return c,d
r1,r2 = add_sub(a,b)
print("Addition Result is = ",r1)
print("Subtraction Result is = ",r2)
