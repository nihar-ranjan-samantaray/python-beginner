arr = []
n = int(input("Enter size of array : "))
print("Enter Elements To The Array : ")
for i in range (n):
    arr.append(int(input()))
print(arr)
res = []
for i in range(0,len(arr)):
    for j in range(i+1,i+2):
        print("i",arr[i],i)
        print("j",arr[j],j)
        x = arr[j] - arr [i]
        res.append(x)
print(res)
 
