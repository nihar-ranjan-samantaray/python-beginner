row = int(input("Enter Number Of Rows : "))
for i in range(1,row+1):
    for j in range(row,i-1,-1):
        print(j,end=" ")
    print()
