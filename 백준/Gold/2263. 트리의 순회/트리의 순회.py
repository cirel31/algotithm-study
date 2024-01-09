import sys
sys.setrecursionlimit(10000000)

def build_tree(inorder, postorder, in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    # 포스트오더의 마지막 요소는 현재 서브트리의 루트 노드
    root = postorder[post_end]
    preorder.append(root)

    # 인오더에서 루트 노드의 위치 찾기
    root_idx = inorder_index[root]

    # 왼쪽 서브트리의 크기
    left_size = root_idx - in_start

    # 왼쪽 서브트리 재귀적으로 처리
    build_tree(inorder, postorder, in_start, root_idx - 1, post_start, post_start + left_size - 1)

    # 오른쪽 서브트리 재귀적으로 처리
    build_tree(inorder, postorder, root_idx + 1, in_end, post_start + left_size, post_end - 1)


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# 프리오더 결과를 저장할 리스트
preorder = []

# 인오더에서 각 노드의 인덱스를 저장
inorder_index = {node: idx for idx, node in enumerate(inorder)}

build_tree(inorder, postorder, 0, n - 1, 0, n - 1)

print(*preorder)
