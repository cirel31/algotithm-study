n = int(input())
li = list(map(int, input().split()))

left, right = 0, n-1
res = float('inf')
best = (0, 0)

while left < right:
    mix = li[left] + li[right]
    if abs(mix) < res:
        res = abs(mix)
        best = (li[left], li[right])
    if mix < 0:
        left += 1
    elif mix > 0:
        right -= 1
    else:
        break
print(best[0], best[1])
