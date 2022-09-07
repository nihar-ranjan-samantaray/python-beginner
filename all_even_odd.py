n = int(input("Enter the range"))
print("The Range is ",n)
ch = 'y'
i = 0
while ch == 'y':
    x = int(input("Press 1 to Print Even Numbers And 0 to Print Odd Numbers"))
    if x == 1:
        print ("The Even Numbers Are")
        for i in range(1,n+1):
            if i%2 == 0:
                print(i)
    elif x == 0:
        print ("The Odd Numbers Are")
        for i in range(1,n+1):
            if i%2 != 0:
                print(i)
    else:
        print ("wromg Input")
    ch = input("Press Y To Continue")
