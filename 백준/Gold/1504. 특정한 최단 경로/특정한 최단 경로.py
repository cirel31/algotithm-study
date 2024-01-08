import sys
from heapq import heappush, heappop


def solve(start):
    que = []
    distance = [inf for _ in range(N+1)]
    distance[start] = 0
    heappush(que, (start, 0))
    while que:
        idx, length = heappop(que)
        if length > distance[idx]:
            continue
        for now, weight in graph[idx]:
            dt = length + weight
            if dt < distance[now]:
                distance[now] = dt
                heappush(que, (now, dt))
    return distance


input = sys.stdin.readline
N, E = map(int, input().split())
inf = 1e9
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

# 다익스트라 알고리즘을 통해 시작 위치에 따른 최단 경로 결과 계산
basic = solve(1)
start_v1 = solve(v1)
start_v2 = solve(v2)

# 두 가지 경로 계산: 1 -> v1 -> v2 -> N, 1 -> v2 -> v1 -> N 후 최단 결과 반영
rst_1 = basic[v1] + start_v1[v2] + start_v2[N]
rst_2 = basic[v2] + start_v1[N] + start_v2[v1]
ans = min(rst_1, rst_2)
print(ans if ans < inf else -1)
