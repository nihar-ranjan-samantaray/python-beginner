a = 5
b = 2
try:
    print("Open")
    print(a/b)
    k = int(input())
    print(k)
except ZeroDivisionError as e:
    print("Error\n",e)
except ValueError as e:
   print("Invalid Input\n",e)
except Exception as e:
    print("Something Error\n",e)
finally:
    print("Close")
print("Bye")
