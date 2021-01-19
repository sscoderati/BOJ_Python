n = int(input())
for i in range(n):
    modif = list(map(str,input().split()))
    result = float(modif[0])
    for j in range(len(modif)):
        if modif[j] == '@':
            result *= 3
        elif modif[j] == '#':
            result -= 7
        elif modif[j] == '%':
            result += 5
        else : pass
    print(format(result, ".2f"))


