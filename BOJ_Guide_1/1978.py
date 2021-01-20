def is_prime_number(n):
    if n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if is_prime_number(arr[i]) == True:
        cnt += 1
    else:
        continue
print(cnt)
