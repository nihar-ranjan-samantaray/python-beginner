#from array import *
def insertionsort(arr,n):
    "Insertion Sort"
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key :
            arr[j+1] = arr[j]
            j = j-1
            arr[j+1] = key
    print("Array After Sorting : {}".format(arr))

n = int(input("Enter Size of Array : "))
#arr = array('i',[])
arr = []
print("Enter Elements in the Array : ")
for i in range(n):
    x = int(input())
    arr.append(x)
print("Array before Sorting {}".format(arr))
insertionsort(arr,n)
