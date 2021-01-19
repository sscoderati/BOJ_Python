n = int(input())
C = 100
S = 100
for i in range(n):
    m, k = map(int,input().split())
    if m > k:
        S -= m
    elif k > m:
        C -= k
    else:
        continue
print(C)
print(S)
