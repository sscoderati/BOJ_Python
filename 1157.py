import sys

s = input()
tmp = 0
for i in range(len(s) - 1):
    if s.count(s[i + 1]) > s.count(s[tmp]):
        tmp = i + 1
    elif((s[tmp] != s[i + 1]) and (s.count(s[i + 1]) == s.count(s[tmp]))):
        print('?')
        sys.exit()
    else:
        continue

print(s[tmp])
