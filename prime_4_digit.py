# Program To Print Highest 4 Digit Prime Number
# Nihar Ranjan Samantaray
# 02 - OCT - 1996

def isprime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    else:
        prime.append(n)   #Store All Prime Numbers In The Array
        return True

prime = []
for i in range(1000,10000): #Range Of All 4 Digit Numbers
    isprime(i)
    
print(prime,end="")  #Print All Prime Numbers

#Checking Highest Number
for i in range(len(prime)):
    for j in range(len(prime)):
        if prime[i] > prime[j]:
            large = prime[i]   #Highest Number
print("Largest Prime Number is",large)  #Print Highest Prime Number

