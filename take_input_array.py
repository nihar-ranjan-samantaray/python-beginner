#Take Input From User And Display in An Array

n = int(input("Enter Size Of Array : "))
arr = []
print("Enter Elements To Array")
for i in range(int(n)):
    x = int(input())
    arr.append(x)
print("The Elements Of The Array Are",arr,"\n")

val = int(input("Enter The Element For Search : \n"))

for e in arr:
    if e == val:
       print("{} is Present in Position {}".format(val,arr.index(e)))
       break
else:
        print("{} is not Present".format(val))
