n = int(input("Enter Any Number"))
count = 0
for i in range(2,n+1):
    if n % i == 0:
        count = count + 1
if count == 1:
    print(n,"is Prime")
else:
    print(n,"is Composite")
