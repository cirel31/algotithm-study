def solve():
    res = []
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    que = [(0, 0, 1)]
    while que:
        x, y, cnt = que.pop(0)
        for dx, dy in delta:
            nx, my = x + dx, y + dy
            if (0 <= nx < n and 0 <= my < m) and li[nx][my] and not visited[nx][my]:
                que.append((nx, my, cnt+1))
                visited[nx][my] = 1
            if nx == n-1 and my == m-1:
                res.append(cnt+1)
    return min(res)


n, m = map(int, input().split())
li = [list(map(int, input().strip())) for _ in range(n)]
ans = solve()
print(ans)
