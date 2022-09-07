def fibonacci(n):
    f1 = 0
    f2 = 1
    for i in range(1,n+1):
        temp = f1 + f2
        f1 = f2
        f2 = temp
    print(f1)
def prime(n):
    
    for i in range(2,100):
        flag = 0
        count = 0
        for j in range(2,i):
            if i % j == 0:
                flag == 1
                break
        count = count + 1
        if flag == 0:
            print(i)
            break
            
n = int(input("Enter The Place : "))

if n%2 == 1:
    fibonacci(n//2 + 1)
else:
    prime(n//2)
