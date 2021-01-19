H, M = map(int, input().split())
if M >= 45:
    print(H, M-45)
else:
    H-=1
    M+=60
    if H < 0:
        H+=24
    else:
        pass
    print(H, M-45)
