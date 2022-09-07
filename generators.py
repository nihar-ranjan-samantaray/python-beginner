
class inclusive_range:
    def __init__(self, *args):
        numargs = len(args)
        if numargs < 1: raise TypeError("At least one argument Required")
        elif numargs == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numargs == 2:
            (self.start,self.stop) = args
            self.step = 1
        elif numargs == 3:
            (self.start,self.stop,self,step) = args
        else: raise ValueError("Expected 3 arguments but {} arguments inputed".format(numargs))
    def __iter__(self):
        i = self.start
        while i <= self.stop:
            yield i
            i += self.step


def main():
    ch = 'y'
    while ch == 'y' or 'Y':
        a = int(input("Enter Start Point : "))
        b = int(input("Enter Stop Point : "))
        #c = int(input("Step : "))
        for i in inclusive_range(a,b):print(i,end=" ")
        print()
        ch = input("Enter Any Key to Contiue...")
    for i in inclusive_range(5,25):print(i,end=" ")
        
    
if __name__ == "__main__": main()
