# 21:20 - 22:15
import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

dij = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]    # 델타 탐색
complete_omok = ['o', 'o', 'o', 'o', 'o']   # 오목인 상황


def is_omok(arr):
    for row in range(N):    # 행 반복
        for col in range(N):    # 열 반복
            for di, dj in dij:  # 델타 탐색
                omok_check = []  # 오목인지 확인하는 리스트
                for r in range(5):  # 델타 탐색으로 5개의 돌을 리스트에 저장
                    ni = row + di * r
                    nj = col + dj * r
                    if row + di * 4 < 0 or row + di * 4 >= N or col + dj * 4 < 0 or col + dj * 4 >= N:
                        continue
                    omok_check.append(arr[ni][nj])
                if omok_check == complete_omok:  # 5개의 돌을 저장한 리스트가 오목이라면
                    return 1    # 1 return
    return 0    # 0 return


for test_case in range(T):
    N = int(input())
    omok_arr = [list(input()) for _ in range(N)]
    if is_omok(omok_arr):
        print(f'#{test_case+1} YES')
    else:
        print(f'#{test_case+1} NO')

