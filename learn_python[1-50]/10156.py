n, m, k = map(int, input().split())
if n * m > k:
    res = n*m - k
    print(res)
elif n * m < k:
    print(0)
else:
    print(0)
