ch = 'y'
s = 0
count = 0

while ch == 'y':
    n = int(input("Enter A Number : "))
    s = s + n 
    count = count + 1
    ch = input("Do You Want Enter More Number : ")
avg = s // count
print("Average is ",avg)
