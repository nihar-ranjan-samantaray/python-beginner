#Find Out Largest Number Between 3 Numbers Using argv
#NIhar Ranjan Samantarary

x = int(input('Enter 1st Number'))
y = int(input('Enter 2nd Number'))
z = int(input('Enter 3rd Number'))

if x>y:
    if x>z:
        print(x,'is greater')
    else:
        print(z,'is greater')
else:
    if y>z:
        print(y,'is greater')
    else:
        print(z,'is greater')
        
