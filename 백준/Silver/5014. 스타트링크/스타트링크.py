from _collections import deque


def solve():
    que = deque()
    que.append(S)
    visited[S] = 1
    while que:
        x = que.popleft()
        if x == G:
            return visited[x] - 1
        else:
            for i in [x + U, x - D]:
                if 1 <= i <= F and not visited[i]:
                    visited[i] = visited[x] + 1
                    que.append(i)
    return 'use the stairs'


F, S, G, U, D = map(int, input().split())
visited = [0 for _ in range(F+1)]
ans = solve()
print(ans)
