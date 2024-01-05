def solve(a, b):
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    que = [(a, b)]
    while que:
        x, y = que.pop(0)
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if (0 <= ny < m and 0 <= nx < n) and not visited[nx][ny] and li[nx][ny]:
                que.append((nx, ny))
                visited[nx][ny] = 1
    return 1

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    li = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        i, j = map(int, input().split())
        li[i][j] = 1
    visited = [[0 for _ in range(m)] for _ in range(n)]
    res = []
    for i in range(n):
        for j in range(m):
            if li[i][j] and not visited[i][j]:
                visited[i][j] = 1
                res.append(solve(i, j))
    print(len(res))
