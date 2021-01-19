n = int(input())
c = 0
nc = 0

for i in range(n):
    v = int(input())
    if v > 0:
        c+=1
    else:
        nc+=1
if c > nc:
    print("Junhee is cute!")
elif nc > c:
    print("Junhee is not cute!")
