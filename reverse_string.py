string = input("Enter Your String : ")
rev = str
length = len(string)
j = length - 1
for i in range(0,length+1):
    rev = string[j]
    j -= 1
    print(rev,end="")

