def addition(n):
    return n*2
num1 = [1,2,3,4]
num2 = [3,5,7,9]
res = list(map(addition,num1))
print(res)

res2 = list(map(lambda x: x * x, num1))
print(res2)

res3 = list(map(lambda x,y: x + y, num1, num2))
print(res3)

str1 = '12345'
res4 = list(map(list, str1))
print(res4)