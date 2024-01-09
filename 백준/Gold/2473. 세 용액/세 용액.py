import sys

input = sys.stdin.readline
n = int(input())
li = list(map(int, input().split()))
li.sort()
res = float('inf')
best = None

for i in range(n-2):
    left, right = i+1, n-1

    while left < right:
        mix = li[left] + li[right] + li[i]
        if abs(mix) < res:
            res = abs(mix)
            best = (li[i], li[left], li[right])
        if mix < 0:
            left += 1
        elif mix > 0:
            right -= 1
        else:
            break
print(best[0], best[1], best[2])
