import sys, heapq

input = sys.stdin.readline
V, E = map(int, input().split())
k = int(input())
inf = 1e9
que = []  # 우선순위 큐 (힙) 초기화
graph = [[] for _ in range(V+1)]  # 각 정점에 연결된 간선을 저장할 그래프 초기화
distance = [inf for _ in range(V+1)]  # 각 정점까지의 최단 거리를 저장할 배열 초기화
distance[k] = 0  # 시작 정점의 거리는 0으로 설정

# 모든 간선 정보를 입력받아 그래프를 구성
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 우선순위 큐에 시작 정점을 넣음 (거리, 정점)
heapq.heappush(que, (0, k))

# 우선순위 큐가 빌 때까지 반복
while que:
    length, idx = heapq.heappop(que)  # 가장 거리가 짧은 정점을 선택
    if length > distance[idx]:  # 이미 처리된 정점이면 무시
        continue

    # 현재 정점과 연결된 다른 정점들을 확인
    for now, weight in graph[idx]:
        dt = length + weight  # 선택된 정점을 거쳐 가는 거리
        if dt < distance[now]:  # 더 짧은 경로를 발견하면 업데이트
            distance[now] = dt
            heapq.heappush(que, (dt, now))

# 모든 정점까지의 최단 거리를 출력
for i in distance[1:]:  # distance[0]은 무시
    print(i if i != inf else 'INF')
