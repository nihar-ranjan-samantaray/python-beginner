f = open('myfile.txt','r')
f1 = open('myfileNew.txt','w')

for i in f:
    f1.write(i)

