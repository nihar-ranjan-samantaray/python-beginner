
def calculate(sec):
    tsec = sec % 60
    
    minn = sec // 60
    
    tminn = minn % 60

    thr = minn // 60

    print("{} Hour {} Minute {} Second".format(thr,tminn,tsec))


sec = int(input("Enter Time In Seconds : "))
#obj = time()

calculate(sec)
