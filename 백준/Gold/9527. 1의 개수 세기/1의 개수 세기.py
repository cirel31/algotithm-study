def setting():
    res = [0] * 64
    res[0] = 1
    for i in range(1, 64):
        res[i] = res[i - 1] * 2 + (1 << i)
    return res


def solve(x):
    ans = x & 1
    for i in range(64, 0, -1):
        if x & (1 << i):
            ans += visited[i - 1] + (x - (1 << i) + 1)
            x -= 1 << i
    return ans


visited = setting()
A, B = map(int, input().split())
print(solve(B) - solve(A - 1))
