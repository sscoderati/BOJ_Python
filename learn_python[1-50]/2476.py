n = int(input())
prize = []

for i in range(n):
    arr = list(map(int, input().split()))
    arr.sort()

    if arr[0] == arr[1] != arr[2]:
        tmp = 1000 + arr[0] * 100
        prize.append(tmp)
    elif arr[0] != arr[1] == arr[2]:
        tmp = 1000 + arr[1] * 100
        prize.append(tmp)
    elif arr[0] == arr[1] == arr[2]:
        tmp = 10000 + arr[0] * 1000
        prize.append(tmp)
    else:
        tmp = arr[2] * 100
        prize.append(tmp)

prize.sort()
print(prize[n - 1])
