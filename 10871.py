n, x = map(int, input().split())
array = list(map(int, input().split()))
small = []
for i in range(n):
    if array[i] < x:
        small.append(array[i])
    else:
        continue
print(*small)
