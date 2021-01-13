n = int(input())

def is_prime(n):
    for i in range(2, n):
        if n != 2 and n % i == 0:
            return False
        else:
            continue
    return True

i = 2
while n != 1:
    if n % i == 0 and is_prime(i) == True:
        n /= i
        print(i)
    else:
        i += 1
