from numpy import *

arr1 = array([10,20,30,40,50,60,70,80])

print ("The Array is {}".format(arr1))
x = int(input("1. Deep Copy\n2. Shallow Copy\n3. Exit\nEneter Your Choice : \n"))
if x == 1:
    arr2 = arr1.copy()
    print("--------Deep Copy---------")
    print("1st Array is {}".format(arr1))
    print("2nd Array is {}".format(arr2))
    arr1[3] = 12
    print("After Changing The Value")
    print("1st Array is {}".format(arr1))
    print("2nd Array is {}".format(arr2))
elif x == 2:
    arr2 = arr1.view()
    print("---------Shallow Copy-------")
    print("1st Array is {}".format(arr1))
    print("2nd Array is {}".format(arr2))
    arr1[3] = 12
    print("After Changing The Value")
    print("1st Array is {}".format(arr1))
    print("2nd Array is {}".format(arr2))
else:
    exit
