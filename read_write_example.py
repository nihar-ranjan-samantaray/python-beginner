read = open("new.txt","r")
write = open("myfile.txt","w")

for i in read:
    print(i,file = write)

