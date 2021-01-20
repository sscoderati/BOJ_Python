from collections import deque

n, k = map(int, input().split())
queue = []
for i in range(1, n + 1):
    queue.append(i)
queue = deque(queue)
print('<', end = '')
for i in range(n):
    for j in range(k - 1):
        queue.append(queue.popleft())
    print(queue.popleft(), end = '')
    if i == n - 1:
        pass
    else:
        print(',', end=' ')
print('>', end ='')

