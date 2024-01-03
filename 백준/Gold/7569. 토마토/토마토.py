from _collections import deque


def solve():
    delta = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    while que:
        z, y, x = que.popleft()
        for dh, dn, dm in delta:
            hz, ny, mx = z + dh, y + dn, x + dm
            if 0 <= hz < H and 0 <= ny < N and 0 <= mx < M:
                if box[hz][ny][mx] == 0 and not visited[hz][ny][mx]:
                    que.append((hz, ny, mx))
                    visited[hz][ny][mx] = 1
                    box[hz][ny][mx] = box[z][y][x] + 1


M, N, H = map(int, input().split())
box = [[] for _ in range(H)]
for i in range(H):
    box[i] = [list(map(int, input().split())) for _ in range(N)]
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
que = deque()
ans = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 1:
                que.append((h, n, m))
                visited[h][n][m] = 1
solve()
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 0:
                print(-1)
                exit()
            ans = max(ans, box[h][n][m])
print(ans - 1)