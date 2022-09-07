def count(lst):
    more = 0
    less = 0
    for i in lst:
        if len(i) >= 5:
            more+= 1
        else:
            less+= 1
    return more,less


lst = ['amit','nihar','ayan','soubhagya','nalita','pammi','sibani']
more,less = count(lst)

print(more)
print(less)
