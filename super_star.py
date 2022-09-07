def prime(n):
    for i in range(2,n):
        if n % i == 0:
            return 0
    else:
        return 1
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

n = int(input("Enter a Number : "))
p = prime(n)
fi = fibonacci(n)
fa = factorial(n)

print("Prime" if p == 1 else "Not Prime")
print(fi)
print(fa)
