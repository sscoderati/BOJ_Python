from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            s_x, s_y = i, j
            array[s_x][s_y] = 0
            break

def bfs(x, y):
    q = deque([(x, y)])
    visited = set([(x, y)])
    time = 0
    shark = 2
    cnt = 0
    check = False

    result = 0

    while q:
        size = len(q)
        q = deque(sorted(q))

        for _ in range(size):
            x, y = q.popleft()

            if array[x][y] != 0 and array[x][y] < shark:
                array[x][y] = 0
                cnt += 1
                if cnt == shark:
                    shark += 1
                    cnt = 0
                q, visited = deque(), set([(x, y)])
                check = True

                result = time
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    if array[nx][ny] <= shark:
                        q.append((nx, ny))
                        visited.add((nx, ny))
            if check:
                check = False
                break
        time += 1
    return result

print(bfs(s_x, s_y))