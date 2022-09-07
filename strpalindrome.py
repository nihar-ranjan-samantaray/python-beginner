def reverse(s):
    return s[::-1]


def isPalindrome(s):
    rev = reverse(s)

    if s == rev:
        return True
    else:
        return False

def main():
    s = input("Entre A String : ")

    ans = isPalindrome(s)

    if ans == 1:
        print("{} is Palindrome".format(s))
    else:
        print("{} is Not Palindrome".format(s))


if __name__ == "__main__" : main()
