def permutation(string,start,end):
    i = 0
    if start == end-1:
        print(string)
    else:
        for i in range(start,end):
            x = list(string)
            temp = x[start]
            x[start] = x[i]
            x[i] = temp

            permutation("".join(x),start+1,end)
            temp = x[start]
            x[start] = x[i]
            x[i] = temp

def main():
    string = input("Enter The String : ")
    n = len(string)
    print("All Permutation of the string are : ")
    permutation(string,0,n)

if __name__ == "__main__":main()
