def solve(key, num):
    global ans
    num += 1
    visited[key] = 1
    if key == b:
        ans = num
    for i in graph[key]:
        if not visited[i]:
            solve(i, num)


n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    p, q = map(int, input().split())
    graph[p].append(q)
    graph[q].append(p)
visited = [0 for _ in range(n+1)]
ans = 0
solve(a, 0)
print(ans - 1)

