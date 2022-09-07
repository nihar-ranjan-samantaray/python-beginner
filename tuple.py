tupp = (1,2,3,4,5)
print(tupp)
print(tupp[-4:-1])
print(len(tupp))

y = list(tupp)
print(y)
y.append(10)
print(y)
tupp = tuple(y)
print(tupp)
for x in tupp:
    print(x)
