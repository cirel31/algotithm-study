
from collections import deque

n, k = map(int, input().split())
count = n
num_li = deque([])
ans_li = []
for i in range(1, n+1):
    num_li.append(i)

while count > 0:
    count -= 1
    for _ in range(k-1):
        num_li.append(num_li.popleft())
    x = num_li.popleft()
    ans_li.append(x)

print('<', end='')
print(*ans_li, sep=', ', end='')
print('>', end='')