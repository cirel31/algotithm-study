def solve(start, end, sum, subsum, isRight):
    if start == end:
        if isRight:
            subsum[sum] = subsum.get(sum, 0) + 1
        else:
            global count
            count += subsum.get(k - sum, 0)
        return

    solve(start + 1, end, sum + arr[start], subsum, isRight)
    solve(start + 1, end, sum, subsum, isRight)


n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
mid = n // 2
subsum = {}
solve(mid, n, 0, subsum, True)
solve(0, mid, 0, subsum, False)
if not k:
    print(count-1)
else:
    print(count)
