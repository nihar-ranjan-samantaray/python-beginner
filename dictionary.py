dicti = {"Name" : "Nihar","Mob" : 9090090892,"Sic" : 170710015}
#print(dicti.count())
print(dicti["Name"])
print(dicti.get("Name"))
print(dicti.keys())
print(dicti.values())
dicti["Sic"] = 12345
dicti["Hey"] = 12345
#for e in dicti:
 #   print(dicti[e])
#for x in dicti.values():
#    print(x)
del dicti ["Name"]
for a,b in dicti.items():
    print(a,b)
dict2 = dict(dicti)
dicti.clear()
for a,b in dicti.items():
    print(a,b)
for a,b in dict2.items():
    print(a,b)
