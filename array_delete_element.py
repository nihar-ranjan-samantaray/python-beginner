
def delete():
    y = int(input("Press 1 to Delete Element from Array...Anykey to Exit : \n"))
    if y == 1:
        d = int(input("Enter the position you want to delete : \n"))
        if d <= n:
            for x in arr:
                del arr[d]
                break
        else:
            print("Out of Index")
    else:
        pass
    print("Updated Array is {}".format(arr))
    
n = int(input("Enter Size Of Array : "))
arr = []
print("Enter Elements To Array")
for i in range(int(n)):
    x = int(input())
    arr.append(x)
print("The Elements Of The Array Are",arr,"\n")
delete()
