n = int(input())
s = input()
Acnt = 0
Bcnt = 0
for i in range(n):
    if s[i] == 'A':
        Acnt += 1
    elif s[i] == 'B':
        Bcnt += 1
    else:
        continue
if Acnt > Bcnt:
    print('A')
elif Bcnt > Acnt:
    print('B')
else:
    print("Tie")
