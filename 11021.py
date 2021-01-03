T = int(input())
result = []
first =[]
second = []
for i in range(T):
    case = list(map(int, input().split()))
    first.append(case[0])
    second.append(case[1])
    tmp = case[0] + case[1]
    result.append(tmp)
for i in range(T):
    print("Case #%d: %d + %d = %d" %(i+1, first[i], second[i], result[i]))
