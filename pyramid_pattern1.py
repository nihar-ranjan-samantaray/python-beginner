row = int(input("Enter Number Of Rows : "))
for i in range(1,row+1):
    k = 0
    for space in range(0,row-i):
        print(" ",end="")
    while( k != 2*i - 1):
        print("*",end="")
        k += 1
    print()
