while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    elif n <= m:
        print("No")
    else:
        print("Yes")
