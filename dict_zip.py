files = ['A','B','C']
links = ['X','Y','Z']

result = dict(zip(files,links))
print(result)


list1 = []
dict1 = {}

for _ in range(len(links)):
    dict1['file'] = files[_]
    dict1['link'] = links[_]
    list1.append(dict1.copy())

print(list1)