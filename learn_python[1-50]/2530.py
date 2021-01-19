A, B, C= map(int, input().split())
D = int(input())
C += D
while C > 59:
    C -= 60
    B += 1
    if B > 59:
        B = 0
        A += 1
        if A > 23:
            A = 0
print(A, B, C)
