sett = {1,2,3,45,5,5}
print(sett)

for i in sett:
    print(i)
print(1 in sett)
sett.add("Hey")
print(sett)
sett.update(["you","are","beautiful"])
print(sett)
sett.pop()
print(sett)
sett.remove(2)
print(sett)
sett.discard(3)
print(sett)
set2 = {1,2,3,45,5,5}
sett.update(set2)
print(sett)
set3 = sett.union(set2)
print(set3)
