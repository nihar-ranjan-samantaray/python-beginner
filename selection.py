#from array import *
def selectionsort(A,n):
    "Selection Sort"
    for i in range(0,n):
        minn = A[i]
        loc = i
        for j in range(i + 1,n):
            if minn > A[j]:
                minn = A[j]
                loc = j
                if loc != i:
                    temp = A[i]
                    A[i] = A[loc]
                    A[loc] = temp
        
        
    print("Array After Sorting : {}".format(A))

n = int(input("Enter Size of Array : "))
#arr = array('i',[])
arr = []
print("Enter Elements in the Array : ")
for i in range(n):
    x = int(input())
    arr.append(x)
print("Array before Sorting {}".format(arr))
selectionsort(arr,n)
