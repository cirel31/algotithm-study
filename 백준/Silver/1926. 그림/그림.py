def solve(a, b):
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    que = [(a, b)]
    cnt = 1
    while que:
        x, y = que.pop(0)
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if (0 <= ny < m and 0 <= nx < n) and not visited[nx][ny] and li[nx][ny]:
                que.append((nx, ny))
                cnt += 1
                visited[nx][ny] = 1
    res.append(cnt)


n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
res = []
for i in range(n):
    for j in range(m):
        if li[i][j] and not visited[i][j]:
            visited[i][j] = 1
            solve(i, j)
print(len(res))
if len(res):
    print(max(res))
else:
    print(0)