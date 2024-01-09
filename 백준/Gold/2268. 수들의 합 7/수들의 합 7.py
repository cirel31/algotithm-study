import sys

# 세그먼트 트리 업데이트
def modify(node, start, end, idx, val):
    if idx < start or idx > end:
        return
    if start == end:
        tree[node] = val
        return
    mid = (start + end) // 2
    modify(node * 2, start, mid, idx, val)
    modify(node * 2 + 1, mid + 1, end, idx, val)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

# 구간 합 쿼리
def sum_query(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return sum_query(node * 2, start, mid, left, right) + sum_query(node * 2 + 1, mid + 1, end, left, right)

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
tree = [0] * (4 * n)
for _ in range(m):
    op, i, j = map(int, input().rstrip().split())
    if op == 0:
        if i > j:
            i, j = j, i
        print(sum_query(1, 0, n-1, i-1, j-1))
    else:
        modify(1, 0, n-1, i-1, j)
