T = int(input())
for i in range(T):
    N = int(input())
    data = []
    for j in range(N):
        input_data = input().split()
        data.append((input_data[0], int(input_data[1])))
    data.sort(key = lambda x:(-x[1], x[0]))
    print(data[0][0])
