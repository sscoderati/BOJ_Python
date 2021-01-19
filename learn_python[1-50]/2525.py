A, B = map(int, input().split())
C = int(input())
B += C
while B > 59:
    B -= 60
    A += 1
    if A > 23:
        A = 0
print(A, B)



