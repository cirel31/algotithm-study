from _collections import deque


def bfs(start, stores, festival):
    que = deque([start])
    visited = {start}
    while que:
        current = que.popleft()
        if abs(current[0] - festival[0]) + abs(current[1] - festival[1]) <= 1000:
            return "happy"
        for store in stores:
            if store not in visited and abs(current[0] - store[0]) + abs(current[1] - store[1]) <= 1000:
                que.append(store)
                visited.add(store)
    return "sad"


t = int(input())
for _ in range(t):
    n = int(input())
    start = tuple(map(int, input().split()))
    stores = [tuple(map(int, input().split())) for _ in range(n)]
    festival = tuple(map(int, input().split()))
    print(bfs(start, stores, festival))
