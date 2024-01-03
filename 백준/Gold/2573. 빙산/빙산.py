from _collections import deque

def melt_iceberg(iceberg, N, M):
    temp = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if iceberg[i][j] > 0:
                for di, dj in delta:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M and iceberg[ni][nj] == 0:
                        temp[i][j] += 1
    for i in range(N):
        for j in range(M):
            iceberg[i][j] = max(0, iceberg[i][j] - temp[i][j])

def count_iceberg_parts(iceberg, N, M):
    visited = [[False]*M for _ in range(N)]
    part_count = 0
    for i in range(N):
        for j in range(M):
            if iceberg[i][j] > 0 and not visited[i][j]:
                bfs(iceberg, i, j, visited, N, M)
                part_count += 1
    return part_count

def bfs(iceberg, x, y, visited, N, M):
    que = deque([(x, y)])
    visited[x][y] = True
    while que:
        cx, cy = que.popleft()
        for dx, dy in delta:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and iceberg[nx][ny] > 0:
                visited[nx][ny] = True
                que.append((nx, ny))

N, M = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(N)]
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
year = 0
while True:
    year += 1
    melt_iceberg(iceberg, N, M)
    parts = count_iceberg_parts(iceberg, N, M)
    if parts == 0:
        print(0)
        break
    if parts > 1:
        print(year)
        break
