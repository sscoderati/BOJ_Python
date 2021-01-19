import sys

while(True):
    n = int(input())
    if n == -1:
        sys.exit()
    elif n == 1:
        print("1 is NOT perfect.")
    else:
        array = []
        for i in range(2, n):
            if n % i == 0:
                array.append(i)
            else:
                continue
        if sum(array) + 1 == n:
            print(str(n) + " =", end = ' ')
            result = '1'
            for i in range(len(array)):
                result += " + " + str(array[i])
            print(result.rstrip(' '))
        else:
            print(str(n) + " is NOT perfect.")
