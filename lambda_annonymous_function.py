add = lambda a,b : a + b
sub = lambda a,b : a - b
a = int(input("Enter a : \n"))
b = int(input("Enter b : \n"))
res1 = add(a,b)
res2 = sub(a,b)
print("{} + {} = {}".format(a,b,res1))
print("{} - {} = {}".format(a,b,res2))
