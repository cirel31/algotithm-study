import sys

# 세그먼트 트리 구축
def build_segment_tree():
    # 리프 노드 초기화
    for i in range(n):
        tree[n + i] = arr[i]
    # 내부 노드 구축
    for i in range(n - 1, 0, -1):
        tree[i] = tree[i * 2] + tree[i * 2 + 1]

# 세그먼트 트리 업데이트
def update_segment_tree(idx, val):
    idx += n
    tree[idx] = val
    while idx > 1:
        idx //= 2
        tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]

# 구간 합 쿼리
def sum_query(left, right):
    left += n
    right += n
    sum_val = 0
    while left < right:
        if left % 2:
            sum_val += tree[left]
            left += 1
        if right % 2:
            right -= 1
            sum_val += tree[right]
        left //= 2
        right //= 2
    return sum_val


input = sys.stdin.readline
n, m = map(int, input().split())
arr = [0] * n  # 초기 배열
tree = [0] * (2 * n)  # 세그먼트 트리

build_segment_tree()

for _ in range(m):
    op, i, j = map(int, input().split())
    if op == 0:
        if i > j:
            i, j = j, i
        print(sum_query(i - 1, j))
    else:
        update_segment_tree(i - 1, j)
