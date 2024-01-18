from collections import deque
import sys

input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    visited[start] = 1
    while queue:
        v = queue.popleft()
        for u in graph[v]:
            if visited[u] == 0:
                visited[u] = -visited[v]
                queue.append(u)
            elif visited[u] == visited[v]:
                return False
    return True


k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    is_bipartite = True
    for i in range(1, v + 1):
        if visited[i] == 0:
            if not bfs(i):
                is_bipartite = False
                break

    print("YES" if is_bipartite else "NO")
