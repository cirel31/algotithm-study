from _collections import deque


def solve(a, b):
    que = deque()
    que.append((a, b))
    while que:
        x, y = que.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if (0 <= nx < n and 0 <= ny < n) and not visited[nx][ny] and (li[x][y] == li[nx][ny]):
                visited[nx][ny] = 1
                que.append((nx, ny))
    return 1


n = int(input())
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
li = [list(input().strip()) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
ans = [0, 0]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j]
            ans[0] += solve(i, j)
for i in range(n):
    for j in range(n):
        if li[i][j] == 'R':
            li[i][j] = 'G'
visited = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j]
            ans[1] += solve(i, j)
print(*ans)
