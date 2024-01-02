def solve(a, b):
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    que = [(a, b)]
    cnt = 0
    while que:
        x, y = que.pop(0)
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if (0 <= ny < n and 0 <= nx < n) and not visited[nx][ny] and li[nx][ny]:
                que.append((nx, ny))
                cnt += 1
                visited[nx][ny] = 1
    if cnt == 0:
        cnt = 1
    res.append(cnt)


n = int(input())
li = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
res = []
for i in range(n):
    for j in range(n):
        if li[i][j] and not visited[i][j]:
            solve(i, j)
res.sort()
print(len(res))
for k in res:
    print(k)