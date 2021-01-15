n = int(input())
for i in range(n):
    r, e, c = map(int,input().split())
    if r < (e - c):
        print("advertise")
    elif r == (e - c):
        print("does not matter")
    elif r > (e - c):
        print("do not advertise")

