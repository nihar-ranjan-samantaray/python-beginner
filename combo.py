

def combo(A):
    boy = A[0]
    girl = A[1]
    g = A[2] // 2
    r1 = boy - g
    r2 = girl - g
    

    fact1 = fact(boy)
    fact2 = fact(girl)
    fact3 = fact(r1)
    fact4 = fact(r2)
    fact5 = fact(g)
    
    
    m = fact1 //(fact3 * fact5)
    n = fact2 // (fact4 * fact5)
    res = m * n
    
    
    res = res * 2
    print(res)


def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print("Enter No. Of Boys, Girls And Group Size in Multiple Of 2 Respectively : ")
A = []
for x in range(3):
    x = int(input())
    A.append(x)

combo(A)

