def sameElementSearch(arr1, arr2, m, n):
     
    for i in range(m):
        count = 0
        for j in range(n):
            if (arr2[j] == arr1[i]):
                count+= 1
                j_pos = j
        if count == 0:
            print(f"{arr1[i]} - NA")
        else:
            print(f"{arr1[i]} - {j_pos}")
    
arr1 = ['A','B','C','D']
arr2 = ['P','Q','A','D']
m = len(arr1)
n = len(arr2)
sameElementSearch(arr1, arr2, m, n)