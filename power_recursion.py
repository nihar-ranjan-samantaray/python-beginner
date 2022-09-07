def poww(x,y):
    if x == 1:
        return 1
    if y == 1:
        return x
    return x * poww(x,y-1)

x = int(input())
y = int(input())
r = poww(x,y)

print(r)
