import sys

s = input()
if len(s) == 1:
    print(1)
    sys.exit()
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
    print(1)
else:
    print(0)
