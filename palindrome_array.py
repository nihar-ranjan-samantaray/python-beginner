arr = []
n = int(input("Enter Size Of Array : "))
print("Enter Element To Array : ")
for i in range(0,n):
    arr.append(int(input()))
print(arr)
flag = 0
i = 0
while i <= n//2 and n != 0:
    if arr[i] != arr[n-i-1]:
        flag = 1
        break
    i += 1
if flag == 1:
    print("The Array is Not palindrome")
else:
    print("The Array is palindrome")
