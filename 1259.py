import sys

def is_palindrome(s):
    if len(s) == 1:
        print("yes")
        return False
    origin = []
    inverse = []
    if len(s) % 2 == 0:
        for i in range(len(s)//2):
            origin.append(s[i])
        for i in range(len(s)//2, len(s)):
            inverse.append(s[i])
        origin.reverse()
    else:
        for i in range(len(s)//2):
            origin.append(s[i])
        for i in range(len(s)//2 + 1, len(s)):
            inverse.append(s[i])
        origin.reverse()
    if origin == inverse:
        print("yes")
    else:
        print("no")
    return False

while True:
    n = input()
    if n  == '0':
        sys.exit()
    else:
        is_palindrome(n)
