def maximumLenSubArray(arr1, n):
    count=1
    occur=0
    for i in range(0,n - 1):
        if arr1[i] == arr1[i + 1]:
            count += 1
        else:
            count = 1
        if occur < count:
            occur = count
    return occur
arr1 = [1, 2, 3, 4, 5, 5, 5, 5, 5, 2, 2, 1, 1]
n = len(arr1)
print(maximumLenSubArray(arr1, n))