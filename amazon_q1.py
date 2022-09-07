import re

def Compute(input1):
    if input1[0] == chr(88):
        m = int(input1[1])
        n = int(input1[2])
        x = input1[0]
        x = n - m
        return x
    if input1[1] == chr(88):
        m = int(input1[0])
        x = input1[1]
        n = int(input1[2])
        x = n - m
        return x
    if input1[2] == chr(88):
        m = int(input1[0])
        x = input1[2]
        n = int(input1[1])
        x = m + n
        return x

def main():
    expr = "X+7=97"
    print("The Expression is : {}".format(expr))
    input2 = expr

    input1 = re.findall(r"[\w]+",input2)
    print()
    print(input1)
    x = Compute(input1)
    print("X = {}".format(x))

if __name__=="__main__" : main()

