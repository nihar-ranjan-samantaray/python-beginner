import random
r1 = int(input("Enter row size of Matrix 1 : "))
c1 = int(input("Enter column size of Matrix 1 : "))

m1 = []

print("Enter Elements Row Wise\n")
for i in range(r1):
    a1 = []
    for j in range(c1):
        a1.append(int(input()))
    m1.append(a1)
print("Matrix 1 is : \n")
for i in range(r1):
    for j in range(c1):
        print(m1[i][j],end=" ")
    print()

r2 = int(input("Enter row size of Matrix 2 : "))
c2 = int(input("Enter column size of Matrix 2 : "))

m2 = []
print("Enter Elements Row Wise : \n")
for i in range(r2):
    a2 = []
    for j in range(c2):
        a2.append(int(input()))
    m2.append(a2)
print("Matrix 2 is : \n")
for i in range(r2):
    for j in range(c2):
        print(m2[i][j],end=" ")
    print()
if c1 == r2:
    m3 = [[random.random()for col in range(c2)]for row in range(r1)]
    for i in range(r1):
        for j in range(c2):
            m3[i][j] = 0
            for k in range(r2):
                m3[i][j] = m1[i][k] * m2[k][j]
    print("The Resultant Matrix is : ")
    for i in range(r1):
        for j in range(c2):
            print(m3[i][j],end=" ")
        print()
else:
    print("Matrix Multiplication Can Not be Possible")
print()
if r1 == r2 and c1 == c2:
    m4 = [[random.random()for col in range(c1)]for row in range(r1)]

    for i in range(r1):
        for j in range(c2):
            m4[i][j] = m1[i][j] + m2[i][j]
    print("\nThe Resultant Matrix is : ")
    for i in range(r1):
        for j in range(c2):
            print(m4[i][j],end=" ")
        print()
else:
    print("Matrix Addition Can Not be Possible")
 
