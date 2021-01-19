import sys
while(True):
    M, F = map(int, input().split())
    if M == 0 and F == 0:
        sys.exit()
    else:
        print(M + F)
