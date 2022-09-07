

mat = []
r = int(input("Enter Row Of Matrix : \n"))
c = int(input("Enter Column Of Matrix : \n"))
print("Enter Element to Matrix {} Row Wise : \n")
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    mat.append(a)
print("The Resultant {}x{} is {}".format(r,c,mat))
