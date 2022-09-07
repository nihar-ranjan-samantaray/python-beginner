def isPrime(n):
    if n == 1:
        print("{} is Special Number".format(n))
    for x in range(2,n):
        if n % x == 0:
            print("{} Equals {} x {} ".format(n,x,n//x))
            return False
    else:
        print("{} is Prime Number".format(n))
        return True
#a = int(input("Enter Starting Range : "))
#b = int(input("Enter Ending Range : "))
for i in range(1,20):
    isPrime(i)
