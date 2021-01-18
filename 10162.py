import sys
T = int(input())
ant = 0
bnt = 0
cnt = 0
while(T != 0):
    if T % 10 != 0:
        print(-1)
        sys.exit()
    else:
        if T >= 300:
            T -= 300
            ant += 1
        elif T >= 60 and T < 300:
            T -= 60
            bnt += 1
        elif T >= 10 and T < 60:
            T -= 10
            cnt += 1
print(ant, end=' ')
print(bnt, end=' ')
print(cnt, end=' ')
