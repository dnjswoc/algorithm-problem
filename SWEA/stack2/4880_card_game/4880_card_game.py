# 23:30 -
import sys
sys.stdin = open('input.txt', 'r')


def grouping(arr, s):
    s.append(arr)
    if len(arr) <= 2:
        return
    v = s.pop()
    grouping(v[0: len(v) // 2], s)
    grouping(v[len(v) // 2:], s)


T = int(input())

for test_case in range(T):
    N = int(input())
    rsp_arr = list(map(int, input().split()))
    stack = []
    grouping(rsp_arr, stack)
    print(stack)

    for game in stack:
        if len(game) == 2:
            if game[0] == game[1] or game[0] - game[1] == -2 or game[0] - game[1] == 1:
                game.pop()
            else:
                game.pop(0)
    print(stack)


