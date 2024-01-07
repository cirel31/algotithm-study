import sys
from _collections import deque


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
        if len(res) > 0:
            print(res[0])
            res.popleft()
        else:
            print(-1)
    elif x[0] == 4:
        if len(res) > 0:
            print(res[-1])
            res.pop()
        else:
            print(-1)
    elif x[0] == 5:
        print(len(res))
    elif x[0] == 6:
        if len(res) > 0:
            print(0)
        else:
            print(1)
    elif x[0] == 7:
        if len(res) > 0:
            print(res[0])
        else:
            print(-1)
    elif x[0] == 8:
        if len(res) > 0:
            print(res[-1])
        else:
            print(-1)
