lst = ["football","f,fat,tball,foot,bal,foo,balll"]

lst1 = lst[0]
rest = [a for a in lst[1].split(",")]

print (lst1)
print (rest)
res = str
for mid in range(1,len(lst1)):
    if lst1[:mid] in rest and lst1[mid:] in rest:
        res = lst1[:mid]+","+lst1[mid:]
print(res)
