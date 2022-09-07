from array import *
arr = array('i',[2,4,8,16,32])
newArr = array(arr.typecode,(x*x for x in arr))

print(arr)

for i in arr:
    print(i)
print()

for i in newArr:
    print(i)
