def fibonacci(n):
    if n ==0:
        return 0
    if n == 1:
        return 1
    arr.append(n)
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter the nth Term : "))

s = fibonacci(n)
print("the index {} of Factoroial series is {}".format(n,s))
