# 23:50 - 00:15
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

dij1 = [[0, 1], [1, 0], [0, -1], [-1, 0]]   # + 방향 탐색
dij2 = [[1, 1], [1, -1], [-1, -1], [-1, 1]]  # x 방향 탐색

for test_case in range(T):
    N, M = map(int, input().split())
    fly_arr = [list(map(int, input().split())) for _ in range(N)]
    max_fly = 0     # 최대 잡으 수 있는 파리
    for row in range(N):    # 행 반복
        for col in range(N):    # 열 반복
            plus_sum, multiple_sum = fly_arr[row][col], fly_arr[row][col]   # +, x 방향 합계
            max_sum = 0
            for r in range(1, M):
                for di, dj in dij1:  # + 방향 합계
                    if row + (di * r) < 0 or row + (di * r) >= N or col + (dj * r) < 0 or col + (dj * r) >= N:
                        continue
                    plus_sum += fly_arr[row + (di * r)][col + (dj * r)]
                for di, dj in dij2:  # x 방향 합계
                    if row + (di * r) < 0 or row + (di * r) >= N or col + (dj * r) < 0 or col + (dj * r) >= N:
                        continue
                    multiple_sum += fly_arr[row + (di * r)][col + (dj * r)]
            if max_fly < plus_sum:
                max_fly = plus_sum
            if max_fly < multiple_sum:
                max_fly = multiple_sum
    print(f'#{test_case+1} {max_fly}')
