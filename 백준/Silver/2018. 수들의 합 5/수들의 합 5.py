n = int(input())

start, end = 1, 1
res = 0
ans = 0

while end <= n+1:
    if res < n:
        res += end
        end += 1
    elif res == n:
        ans += 1
        res += end
        end += 1
    else:
        res -= start
        start += 1

print(ans)
