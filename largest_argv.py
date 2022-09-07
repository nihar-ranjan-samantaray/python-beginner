#Find Out Largest Number Between 3 Numbers Using argv
#NIhar Ranjan Samantaray

import sys
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])
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
        
