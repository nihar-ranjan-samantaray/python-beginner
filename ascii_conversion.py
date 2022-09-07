ch = input("Enter The Character : \n")
key = int(input("Enter The Key Value : \n"))

if ord(ch) >= 65 and ord(ch) <= 90:
    res = ord(ch) + key
    if res <= 90:
        print(chr(res))
    else:
        res = res - 26
        print(chr(res))
if ord(ch) >= 97 and ord(ch) <= 122:
    res = ord(ch) + key
    res = ord(ch) + key
    if res <= 122:
        print(chr(res))
    else:
        res = res - 26
        print(chr(res))
