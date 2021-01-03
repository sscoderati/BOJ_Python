n, m, k = map(int, input().split())
print((n+m)%k)
print(((n%k)+(m%k))%k)
print((n*m)%k)
print(((n%k)*(m%k))%k)

