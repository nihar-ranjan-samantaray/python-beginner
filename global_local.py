a = 10
def update():
    
    a = 8
    print (a)
    globals()['a'] = 12
    print (a)
update()
print (a)
