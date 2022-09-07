

def isTriplet(arr,n):
    j = 0
    for i in range(n-2):
        for k in range(j+1,n):
            for j in range(i+1,n-1):
                x = arr[i] * arr[i]
                y = arr[j] * arr[j]
                z = arr[k] * arr[k]
                if x == y+z or z == x+y or y == x+z:
                    return 1
    return 0
arr = [3,4,5,6,7]
n = len(arr)

ans = isTriplet(arr,n)
print("Triplet" if ans == 1 else "Not Triplet")
