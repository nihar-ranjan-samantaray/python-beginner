n = int(input("Enter Number of rows : "))

for i in range(0,n+1):
    print(' '*i,end='')
    for j in range(n,i,-1):
        print('*',end='')
    print()