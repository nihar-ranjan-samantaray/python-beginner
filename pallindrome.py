import math

def isPalindrome(pallindrome,n):
    rev = 0
    x = n
    while x > 0:
        lstdigit = x % 10
        rev = (rev*10)+lstdigit
        x = x // 10

    if rev == n:
        pallindrome.append(n)
    #    print("{} is a Pallindrome Number".format(n))
        return True
    else:
        return False


def main():
    pallindrome = []
   # n = int(input("Enter Range : "))
    for i in range(0,10000):
        isPalindrome( pallindrome,i)
    print(pallindrome,end=" ")
    print()
    print("Square Pallindromes Are : ")
    for i in range(0,len(pallindrome)):
        if math.sqrt(pallindrome[i]) in pallindrome:
            print(pallindrome[i])

if __name__ == "__main__" : main()
