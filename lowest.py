n = 754839018
temp = n
for i in range(0,10):
    for temp in range(n+1):
        temp = temp // 10
        if temp % 10 == i:
            print(i,end="")
            temp = n
