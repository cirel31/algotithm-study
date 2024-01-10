import bisect, sys


import bisect

n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort()  # a를 기준으로 정렬

# LIS 구성 및 각 요소의 lines 내 인덱스 추적
lis = []  # LIS를 구성하는 b 값들
index_in_lis = [-1] * n  # 각 요소가 LIS의 어느 위치에 있는지 추적

for i, (_, b) in enumerate(lines):
    idx = bisect.bisect_left(lis, b)
    if idx == len(lis):
        lis.append(b)
    else:
        lis[idx] = b
    index_in_lis[i] = idx  # 현재 전깃줄의 LIS 위치 기록

# 실제 LIS 구성원 추적
actual_lis_members = set()
last_idx = len(lis) - 1
for i in range(n - 1, -1, -1):
    if index_in_lis[i] == last_idx:
        actual_lis_members.add(i)
        last_idx -= 1

# LIS에 포함되지 않는 전깃줄의 a 전봇대 위치 찾기
to_remove = set(range(n)) - actual_lis_members

# 결과 출력
print(len(to_remove))
for index in sorted(to_remove):
    print(lines[index][0])

