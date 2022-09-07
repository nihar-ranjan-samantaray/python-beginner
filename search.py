
def search(lst,n):
    i = 0
    for i in range(0,len(lst)):
        if lst[i] == n:
            globals()['pos']=i
            return True
    return False

lst = []
for i in range(5):
    i = lst.append(int(input()))
print(lst)
n = int(input("Enter The Number You Want to Search : "))

if search(lst,n):
    print("found in position",pos+1)
else:
    print("Not found")
if n in lst:
    print("found")
else:
    print("Not Found")
