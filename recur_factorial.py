def recur_factorial(n):
    if n==1:
        return n
    else:
        return n * recur_factorial(n-1)

num = int(input("Enter A Number : "))
if num < 0:
    print("Factorial Of Negative Numbers Can Not Be Determined")
elif num == 0:
    print("Factorial Of 0 is 1")
else:
    print ("Factorial of ",num,"is",recur_factorial(num))
recur_factorial(num)
