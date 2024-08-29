# 23:50 - 00:15

'''
우선 그림을 보자마자 풍선팡과 비슷하게 델타를 쓰면 되겠다고 생각했습니다.
이중 for문으로 행, 열을 순회하면서
M만큼 [상, 하, 좌, 우] 방향으로 더하고, [우상, 우하, 좌하, 좌상] 방향으로 하나 더 구해서
큰 값을 max_fly와 비교하면서 최댓값을 구하면 되겠다고 문제에 접근했습니다.
'''

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

dij1 = [[0, 1], [1, 0], [0, -1], [-1, 0]]   # + 방향 탐색
dij2 = [[1, 1], [1, -1], [-1, -1], [-1, 1]]  # x 방향 탐색

for test_case in range(T):
    N, M = map(int, input().split())
    fly_arr = [list(map(int, input().split())) for _ in range(N)]
    max_fly = 0     # 최대로 잡을 수 있는 파리
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
            if max_fly < plus_sum:  # 최대로 잡을 수 있는 파리의 수를 구함
                max_fly = plus_sum
            if max_fly < multiple_sum:
                max_fly = multiple_sum
    print(f'#{test_case+1} {max_fly}')
