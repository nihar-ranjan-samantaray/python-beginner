def remove(string,char_to_remove):
    counts = string.count(char_to_remove)
    print(counts)
    string = list(string )
    while counts:
        string.remove(char_to_remove)
        counts -= 1
    print("".join(string))
string = "Nihar Ranjan samantaray"
char_to_remove = "a"

remove(string,char_to_remove)
