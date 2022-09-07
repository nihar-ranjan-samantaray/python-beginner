from array import *
def maxx(k):
        for i in range(1,n):
                if arr[i] > k:
                        k = arr[i]
        return k

        
arr = array('i',[])
n = int(input("Enter Size Of Array : \n"))
print("Enter Elements to Array : ")
for i in range(n):
	x = int(input())
	arr.append(x)
print("The Elements Of Array Are {}".format(arr))
k = arr[0]
m = maxx(k)

print("Maximum Element in the Array is",m)
