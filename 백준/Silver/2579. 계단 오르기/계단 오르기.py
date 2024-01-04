n = int(input())
score = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n + 1)

dp[1] = score[1]
if n > 1:
    dp[2] = score[1] + score[2]

for i in range(3, n + 1):
    dp[i] = max(dp[i - 2], dp[i - 3] + score[i - 1]) + score[i]

print(dp[n])
