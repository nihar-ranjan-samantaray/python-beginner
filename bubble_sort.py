#Take Input From User And Display in An Array

n = int(input("Enter Size Of Array : "))
arr = []
print("Enter Elements To Array")
for i in range(int(n)):
    x = int(input())
    arr.append(x)
print("The Elements Of The Array Are",arr,"\n")
print("Sorting Steps\n")
for i in range(1,n+1):
  for j in range(0,n-i):
      if arr[j] > arr [j+1]:
          temp = arr[j]
          arr[j]  = arr[j+1]
          arr[j+1] = temp
          print(arr,"\n")
print("The Elements Of The Array After Sorting",arr)
