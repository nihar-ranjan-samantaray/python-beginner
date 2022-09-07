
def remove(string):
    n = len(string)
    index = 0
    for i in range(0,n):
        for j in range(0,i+1):
            if string[i] == string[j]:
                        break
            if j == i:
                string[index] = string[i]
                index += 1
    return "".join(string[:index])

string = input("Enter String : ")
print("The String is : ",string)
string = list(string)
print("After Removing Duplicate Characters : ")
stri = remove(string)
print(stri)
