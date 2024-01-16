import sys


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
        print(li[start_x][start_y], end='')
    else:
        key = end // 2
        print('(', end='')
        for i in range(2):
            for j in range(2):
                solve(start_x+(key*i), start_y+(key*j), key)
        print(')', end='')


input = sys.stdin.readline
n = int(input())
li = [list(map(int, input().strip())) for _ in range(n)]
ans = []
solve(0, 0, n)
