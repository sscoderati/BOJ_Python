n = int(input())

def is_prime(n):
    for i in range(2, n):
        if n != 2 and n % i == 0:
            return False
        else:
            continue
    return True

while n != 1:
    for i in range(2, n):
        while is_prime(i) == True and n % i == 0:
            n /= i
            print(i)
