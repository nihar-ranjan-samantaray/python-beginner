def reverse(string):
    string = string.split()
    lst = []
    for i in string:
        lst.insert(0,i)
    for i in lst:
        print(i,end=" ")
    print()
    print(" ".join(lst))

def main():
    string = input("Enter A Line : ")
    print("The Reverse of this line is : ")
    reverse(string)

if __name__ == "__main__":main()
