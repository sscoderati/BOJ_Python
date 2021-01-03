import math

def lcm(a, b):
    return a * b //  math.gcd(a, b)
i = 0
x = int(input())
result = list()
while i < x:
    a, b = map(int, input().split())
    result.append(lcm(a, b))
    i += 1

for e in result:
    print(e)
