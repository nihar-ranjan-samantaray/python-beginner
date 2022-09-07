  
def vowel_consonant(n):
    vowel = 0
    consonant = 0
    for i in range(0,len(n)):
        ch = n[i]
        ch.lower()
        print(ch)
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            vowel += 1
        else:
            consonant += 1
    print(vowel)
    print(consonant)



n = input("Enter Any string : ")
vowel_consonant(n)
