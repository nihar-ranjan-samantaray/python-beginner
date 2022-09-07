

def isTriplet(arr,n):
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                x = arr[i] * arr[i]
                y = arr[j] * arr[j]
                z = arr[k] * arr[k]
                if x == y+z or z == x+y or y == x+z:
                    return 1
    return 0
arr = [3,4,9,8,7]
n = len(arr)

ans = isTriplet(arr,n)
print("Triplet" if ans == 1 else "Not Triplet")
