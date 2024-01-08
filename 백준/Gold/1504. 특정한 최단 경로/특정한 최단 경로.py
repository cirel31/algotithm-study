import heapq
import sys


def dijkstra(start):
    queue = []
    distance = [inf] * (n + 1)
    distance[start] = 0
    heapq.heappush(queue, (0, start))
    while queue:
        length, idx = heapq.heappop(queue)
        if length > distance[idx]:
            continue
        for x, y in graph[idx]:
            d = length + y
            if d < distance[x]:
                distance[x] = d
                heapq.heappush(queue, (d, x))
    return distance


n, e = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n+1)]
inf = sys.maxsize
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, sys.stdin.readline().split())

res1 = dijkstra(1)
res2 = dijkstra(v1)
res3 = dijkstra(v2)

rst1 = res1[v1] + res2[v2] + res3[n]
rst2 = res1[v2] + res2[n] + res3[v1]

ans = min(rst1, rst2)
if ans < inf:
    print(ans)
else:
    print(-1)

