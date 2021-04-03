n = int(input())
res = 0

while True:
    if n % 5 == 0:
        res += (n // 5)
        print(res)
        break

    n -= 3
    res += 1

    if n < 3:
        print(-1)
        break
