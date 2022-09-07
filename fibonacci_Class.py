class Fibonacci():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def series(self):
       while(True):
           yield(self.b)
           self.a,self.b = self.a,  self.a + self.b
    

#r = int(input("Enter Range : "))
f = Fibonacci(0,1)

for n in f.series():
    if n > 50: break
    print(n, end=' ')
