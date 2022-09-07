

def main():
    read = open("myfile.txt","r")
    write = open("new.txt","w")
    for i in read:
        print(i,file = write)

if __name__ == "__main__" : main()
