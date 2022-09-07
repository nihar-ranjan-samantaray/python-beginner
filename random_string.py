import random, string
x = 'PSPPA'+''.join(random.choices(string.digits, k=4))+''.join(random.choices(string.ascii_uppercase, k=2))
print(x)