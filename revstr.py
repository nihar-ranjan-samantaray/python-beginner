n = input("Enter a String : ")
c = len(n)
j = c - 1
revstr = str
for i in range(0,c):
    revstr = n[j]
    
    j -= 1
    print(revstr,end="")
