# dp[i] >> 정수 i를 1로 만드는 과정에 필요한 최소 연산 횟수
# 초기값 설정 >> dp[1] = 0
# i % 3 = 0 >> dp[i] = min(dp[i], dp[i/3] + 1)
# i % 2 = 0 >> dp[i] = min(dp[i], dp[i/2] + 1)
# dp[i] = min(dp[i], dp[i-1] + 1)

n = int(input())
dp = [0] * (n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if not (i % 2):
        dp[i] = min(dp[i], dp[i//2] + 1)
    if not (i % 3):
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])
