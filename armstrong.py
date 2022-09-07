n = int(input("Enter A Number : "))
s = 0
temp = n
while temp > 0:
    r = temp % 10
    s = s + (r*r*r)
    #print(s)
    temp = temp // 10
if n == s:
    print(n,"is an Armstrong Number")
else:
    print(n,"is not an Armstrong Number")
