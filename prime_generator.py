
def isPrime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    else:
        return True

def prime(n = 1):
    while(True):
        if isPrime(n) : yield n
        n += 1

b = int(input("Enter Range : "))
for n in prime():
    if n > b : break
    print(n)
