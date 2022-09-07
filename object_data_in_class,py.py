class Bird():
    def __init__(self,**kwargs):
        self.variable = kwargs
    def set_variable(self,k,v):
        self.variable[k] = v
    def get_variable(self,k):
        return self.variable.get(k,None)

def main():
    b = Bird(feet = 2)
    b.set_variable('color' , 'red')
    print(b.get_variable('feet'))
    print(b.get_variable("color"))
if __name__ == "__main__": main()
