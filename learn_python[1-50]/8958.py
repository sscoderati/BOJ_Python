n = int(input())
tmp = 0
for i in range(n):
    total = 0
    s = input()
    for j in range(len(s)):
        if j == len(s) - 1 and s[j] == 'O':
            tmp += 1
            total += tmp
            tmp = 0
        elif s[j] == 'O' and s[j + 1] == 'O':
            tmp += 1
            total += tmp
        elif s[j] == 'O' and s[j + 1] != 'O':
            tmp += 1
            total += tmp
            tmp = 0
        else:
            continue
    print(total)
