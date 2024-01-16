def solve(start_x, start_y, end):
    flag = True
    for i in range(start_x, start_x+end):
        for j in range(start_y, start_y+end):
            if li[i][j] != li[start_x][start_y]:
                flag = False
                break
        if not flag:
            break
    if flag:
        ans[li[start_x][start_y]] += 1
    else:
        key = end // 3
        for i in range(3):
            for j in range(3):
                solve(start_x+(key*i), start_y+(key*j), key)


n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
ans = [0, 0, 0]
solve(0, 0, n)
print(ans[-1])
print(ans[0])
print(ans[1])
