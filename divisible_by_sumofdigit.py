s = 0
for i in range(1,11):
    r = i % 10
    s = s + r
    i = i // 10
    for i in range(1,11):
        if s % i == 0:
            print("post i",i)
            print(s)
