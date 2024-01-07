import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
res = deque()

for _ in range(n):
    x = list(map(int, input().split()))
    if x[0] == 1:
        res.appendleft(x[1])
    elif x[0] == 2:
        res.append(x[1])
    elif x[0] == 3:
        print(res[0] if res else -1)
        if res:
            res.popleft()
    elif x[0] == 4:
        print(res[-1] if res else -1)
        if res:
            res.pop()
    elif x[0] == 5:
        print(len(res))
    elif x[0] == 6:
        print(1 if not res else 0)
    elif x[0] == 7:
        print(res[0] if res else -1)
    elif x[0] == 8:
        print(res[-1] if res else -1)
