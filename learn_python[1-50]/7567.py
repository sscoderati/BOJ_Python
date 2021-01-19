s = input()
res = 10
for i in range(1, len(s)):
    if s[i - 1] == s[i]:
        res += 5
    else:
        res += 10
print(res)
