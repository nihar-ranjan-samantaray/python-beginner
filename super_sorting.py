def bubble(arr,n):
    for i in range(0,n):
        for j in range(0,n):
            print("i",arr[i])
            print("j",arr[j])
            if arr[i] < arr[j]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
    print("The Array is")
    for i in arr:
        print(i,end=" ")
    print()
def insertion(arr,n):
           
arr = []
n = int(input("Enter size of array : "))
print("Enter Elements to the Array : ")
for i in range(n):
    arr.append(int(input()))
print("The Array is")
for i in arr:
    print(i,end=" ")
print()
print("After Insertion Sort : ")
#insertion(arr,n)
print("After Selection Sort : ")
#selection(arr,n)
print("After Bubble Sort : ")
bubble(arr,n)
