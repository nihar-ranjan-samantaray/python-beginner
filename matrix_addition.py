import random

r1 = int(input("Enter Row Size of Matrix 1 : "))
c1 = int(input("Enter Column Size of Matrix 1 : "))
mat1 = []
mat2 = []
print("Enter Elements To Matrix 1: ")
for i in range(r1):
    a1 = []
    for j in range(c1):
        a1.append(int(input()))
    mat1.append(a1)

print("Matrix 1 is : ")
for i in range(r1):
    for j in range(c1):
        print(mat1[i][j],end=" ")
    print()

        
r2 = int(input("Enter Row Size of Matrix 2 : "))
c2 = int(input("Enter Column Size of Matrix 2 : "))
print("Enter Elements To Matrix 2: ")
for i in range(r2):
    a2 = []
    for j in range(c2):
        a2.append(int(input()))
    mat2.append(a2)
print("Matrix 2 is : ")
for i in range(r2):
    for j in range(c2):
        print(mat2[i][j],end=" ")
    print()
if r1 == r2 and c1 == c2:
    m4 = [[random.random()for col in range(c1)]for row in range(r1)]
    for i in range(r1):
        for j in range(c1):
            m4[i][j] = mat1[i][j] + mat2[i][j]
    print("The Resultant Matrix is : ")
    for i in range(r1):
        for j in range(c1):
            print(m4[i][j],end= " ")
        print()






        
