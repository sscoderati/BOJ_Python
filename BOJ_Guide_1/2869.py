import math
A, B, V = map(int, input().split())
last = V - A
real = A - B
cnt = math.ceil(last / real) + 1
print(cnt)
