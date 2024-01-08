import sys


def bellman_ford(start, n, edges):
    distance = [inf for _ in range(n+1)]
    distance[start] = 0

    # 정점 수 - 1번 반복하면서 각 간선에 대해 최단 거리 업데이트
    for i in range(n):
        for u, v, w in edges:
            if distance[u] != inf and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                # n번째 반복에서도 값이 갱신되면 음의 사이클 존재
                if i == n - 1:
                    return -1

    return distance


n, m = map(int, sys.stdin.readline().split())
inf = 1e9
edges = []
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    edges.append((u, v, w))

distances = bellman_ford(1, n, edges)

if distances == -1:
    print(-1)
else:
    for i in range(2, n + 1):
        print(distances[i] if distances[i] != inf else -1)
