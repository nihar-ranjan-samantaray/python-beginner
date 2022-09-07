lst = [1,2,3,4,5,6,87]
print(lst)
lst.append(3)
print(lst)
lst.remove(4)
print(lst)
lst.pop()
print(lst)
lst.insert(1,"Hey")
print(lst)
lst.extend([0,8,6,5,])
print(lst)
del lst[5]
print(lst)
lst2 = lst.copy()
print(lst2)
lst3 = list(lst2)
print(lst3)

for x in lst2:
    lst.append(x)
print(lst)
lst2.extend(lst3)
print(lst2)
