# 입력: n은 배열의 크기, k는 찾고자 하는 부분합
n, k = map(int, input().split())
# 배열의 요소를 입력받음
li = list(map(int, input().split()))

# 누적합과 부분합 개수를 초기화
prefix_sum = 0  # 누적합
count = 0  # 부분합이 k인 부분 배열의 개수
sum_count = {0: 1}  # 누적합이 0인 경우는 기본적으로 1번 존재

# 배열을 순회하면서 누적합을 계산
for num in li:
    prefix_sum += num  # 현재 위치까지의 누적합

    # 누적합에서 k를 뺀 값이 이전에 존재하는지 확인하여 count를 업데이트
    # get(key, default) >> key가 dict에 존재하지 않는다면, default로 지정된 값을 반환
    count += sum_count.get(prefix_sum - k, 0)

    # 현재 누적합의 등장 횟수를 업데이트
    sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1

# 최종적으로 계산된 부분합이 k인 부분 배열의 개수 출력
print(count)
