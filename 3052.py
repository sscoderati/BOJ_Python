arr = []
for i in range(10):
    arr.append(int(input()))
for i in range(10):
    arr[i] %= 42
arr = set(arr)
arr = list(arr)
st = arr[0]
cnt = 1
for i in range(len(arr)):
    if st != arr[i]:
        cnt += 1
print(cnt)
