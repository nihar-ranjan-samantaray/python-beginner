n = int(input("Enter Number of rows : "))
for i in range(n+1):
    for j in range(1,i+1):
        if j == 1 or j == i or i == n:
            print(j,end="")
        else:
            print(" ", end="")
    print("")