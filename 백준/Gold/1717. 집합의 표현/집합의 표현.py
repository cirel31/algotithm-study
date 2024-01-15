import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    A = find(a)
    B = find(b)
    if A < B:
        parent[B] = A
    else:
        parent[A] = B


n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    check, a, b = map(int, input().split())
    if check == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
