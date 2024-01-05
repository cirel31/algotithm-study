from _collections import deque


def solve(a, b, n):
    if a == b:
        return 0
    que = deque([a])
    visited = {a}
    cnt = 0
    while que:
        for _ in range(len(que)):  # 현재 레벨에 있는 모든 노드를 처리
            x, y = que.popleft()
            for dx, dy in move:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    if (nx, ny) == b:
                        return cnt + 1  # 이동 횟수는 현재 레벨에서 한 번 더 이동한 것이므로 cnt+1 반환
                    que.append((nx, ny))
                    visited.add((nx, ny))
        cnt += 1  # 현재 레벨의 모든 노드 처리 완료 후 이동 횟수 증가
    return -1


t = int(input())
move = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
for _ in range(t):
    n = int(input())
    res = []
    now = tuple(map(int, input().split()))
    dist = tuple(map(int, input().split()))
    ans = solve(now, dist, n)
    print(ans)
