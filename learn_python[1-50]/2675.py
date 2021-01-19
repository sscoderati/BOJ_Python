t = int(input())

for i in range(0, t):
    r, s = map(str,input().split())
    p = ""
    for j in range(len(s)):
        p += s[j] * int(r)
    print(p)
