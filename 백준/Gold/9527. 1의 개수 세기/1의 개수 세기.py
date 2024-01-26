def solve(x):
    binary = bin(x)[2:]
    delta = len(binary)
    res = 0
    for i in range(delta):
        if binary[i] == '1':
            idx = delta - i - 1
            res += visited[idx]
            res += (x - 2**idx + 1)
            x = x - 2**idx
    return res


A, B = map(int, input().split())
visited = [0 for _ in range(64)]
for i in range(1, 64):
    visited[i] = 2**(i-1) + 2*visited[i-1]
ans = solve(B) - solve(A-1)
print(ans)