q1 = 0
q2 = 0
q3 = 0
q4 = 0
ax = 0
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        ax += 1
    elif x >= 1 and y >= 1:
        q1 += 1
    elif x <= -1 and y >= 1:
        q2 += 1
    elif x <= -1 and y <= -1:
        q3 += 1
    elif x >= 1 and y <= -1:
        q4 += 1
    else:
        continue
print("Q1: " + str(q1))
print("Q2: " + str(q2))
print("Q3: " + str(q3))
print("Q4: " + str(q4))
print("AXIS: " + str(ax))
