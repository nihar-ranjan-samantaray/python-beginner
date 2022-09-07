

def openf():
    try:
        for x in readf("myFile.txt"):print(x,end="")
    except IOError as e:
        print(e)
    except ValueError as e:
        print(e)
def readf(filename):
    if filename.endswith(".txt"):
        fh = open(filename)
        return fh.readlines()
    else:raise ValueError("File Must Ends With .txt")

openf()
