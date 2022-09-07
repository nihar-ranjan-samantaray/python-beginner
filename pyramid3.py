""" n = int(input())
count = 0
count1 = 0
k = 0
for i in range(1,n+1):
    for j in range(1,n):
        print(" ",end ="")
        count = count+1
    while k!= 2*i-1:
        if count <= n-1:
            print("*",end="")
            count = count+1
        else:
            count1 = count1+1
            print("*",end="")
        k = k+1

    count1 = count = k = 0
    print()
    
 """
 
n = int(input("Enter Number of rows : "))
for i in range(1,n+1):
    for j in range(i,n+1):
        print("*", end='')
    print()