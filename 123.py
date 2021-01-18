import sys
n = sys.stdin.readline().rstrip()
n = int(n)
i = 2
while(n != 1):
    if n % i == 0:
        n /= i
        print(i)
    else:
        i += 1
