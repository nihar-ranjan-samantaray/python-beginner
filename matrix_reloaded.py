import random

mat1 = []
mat2 = []
r1 = int(input("Enter Row Size of Matrix 1 : "))
c1 = int(input("Enter Column Size of Matrix 1 : "))
r2 = int(input("Enter Row Size of Matrix 2 : "))
c2 = int(input("Enter Column Size of Matrix 2 : "))
print("Enter Elements to Matrix 1 : ")
for i in range(r1):
    m1 = []
    for j in range(c1):
        m1.append(int(input()))
    mat1.append(m1)
print("Enter Elements to Matrix 2 : ")
for i in range(r2):
    m2 = []
    for j in range(c2):
        m2.append(int(input()))
    mat2.append(m2)
print("The Matrix 1 is : ")
for i in range(r1):
    for j in range(c1):
        print(mat1[i][j],end=" ")
    print()
print("The Matrix 2 is : ")
for i in range(r2):
    for j in range(c2):
        print(mat2[i][j],end=" ")
    print()
res = 0
if r2 == c1:
    mat_mul = [[random.random() for col in range(c2)]for row in range(r1)]
    for i in range(r1):
        for j in range(c2):
               mat_mul[i][j] = 0
               for k in range(r2):
                   res = res + mat1[i][k] * mat2[k][j]
                   mat_mul[i][j] = res
                   res = 0
    for i in range(r1):
        for j in range(c2):
            print(mat_mul[i][j],end=" ")
        print()
else:
    print("Matrix Multiplication Can Not Possible")
            
