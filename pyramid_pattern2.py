row = int(input("Enter Number Of Rows : "))
count = 0
count1 = 0
for i in range(1,row+1):
    k = 0
    for space in range(0,row-i):
        print(" ",end=" ")
        count += 1
    while( k != 2*i - 1):
        if count <= row - i:
            print(i+k,end=" ")
        else:
            count1 += 1
            print(i+k - 2*count1,end=" ")
        k += 1
    count = 0
    count1 = k = 0
    print()
