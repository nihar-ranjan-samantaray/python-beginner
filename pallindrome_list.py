def palindrome(n):
    s = 0
    temp = n
    while n > 0:
        r = n % 10
        s = s * 10 + r
        n = n // 10
    if s == temp:
        return 1
    else:
        return 0
n = int(input())
arr = []
for i in range(1,1000):
    if palindrome(i):
        if i < n:
            arr.append(i)
for i in arr:
    print(i,end=" ")
