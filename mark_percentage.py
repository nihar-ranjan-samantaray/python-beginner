m1 = int(input("Enter Mark Of Subject 1 : "))
m2 = int(input("Enter Mark Of Subject 2 : "))
m3 = int(input("Enter Mark Of Subject 3 : "))
m4 = int(input("Enter Mark Of Subject 4 : "))
m5 = int(input("Enter Mark Of Subject 5 : "))
m6 = int(input("Enter Mark Of Subject 6 : "))

s = m1 + m2 + m3 + m4 + m5 + m6
a = s / 6
print("Total Mark is ",s)
print(a,"%")
if a > 75:
    if a > 90:
        print("Grade O")
    else:
        print("Grade E")
elif a > 55:
    if a > 65:
        print("Grade A")
    else:
        print("Grade B")
elif a > 35:
    if a > 45:
        print("Grade C")
    else:
        print("Grade D")
else:
    print("Grade F")
