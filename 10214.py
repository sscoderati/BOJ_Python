T = int(input())
for i in range(T):
    yscore = 0
    kscore = 0
    for j in range(9):
        Y, K = map(int,input().split())
        yscore += Y
        kscore += K
    if yscore > kscore:
        print("Yonsei")
    elif kscore > yscore:
        print("Korea")
    else:
        print("Draw")
