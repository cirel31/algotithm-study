from _collections import deque


def solve(p, q):
    que.append((p, q))
    while que:
        x, y = que.popleft()
        for dx, dy in delta:
            nx, my = x + dx, y + dy
            if 0 <= nx < n and 0 <= my < m:
                if area[nx][my] and not visited[nx][my]:
                    que.append((nx, my))
                    visited[nx][my] = 1
                if not area[nx][my]:
                    visited[x][y] += 1


n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
que = deque()
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
ans = 0
while 1:
    visited = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if area[i][j] and not visited[i][j]:
                visited[i][j] = 1
                solve(i, j)
                cnt += 1
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                area[i][j] -= (visited[i][j] - 1)
                if area[i][j] < 0:
                    area[i][j] = 0
    ans += 1
    if not cnt:
        print(cnt)
        exit()
    if cnt >= 2:
        break
print(ans - 1)