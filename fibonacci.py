def fib(n):
    f1 = 0
    f2 = 1
    
    print("The Fibonacci Series of ",n,"is \n")
    print(f1)
    print(f2)
    for i in range(2,n):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        if f3 <= n:
            print(f3)
n = int(input("Enter The Number Whose Fibonnaci Series You Want : "))
fib(n)
